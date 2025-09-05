#!/usr/bin/env python3
"""
PDF Splitter Utility for DP-600 Study Materials

Splits large PDF files into smaller chunks (max 30MB each) for AI processing.
Perfect for breaking down Microsoft study guides into manageable pieces.

Usage:
    python pdf_splitter.py input/large_study_guide.pdf
    python pdf_splitter.py input/large_study_guide.pdf --max-size 25
"""

import os
import sys
import argparse
from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter
import tempfile


def get_file_size_mb(filepath):
    """Get file size in MB"""
    return os.path.getsize(filepath) / (1024 * 1024)


def split_pdf_by_size(input_path, max_size_mb=30):
    """
    Split PDF into chunks that don't exceed max_size_mb
    
    Args:
        input_path (str): Path to input PDF file
        max_size_mb (int): Maximum size per chunk in MB (default: 30)
    
    Returns:
        list: Paths to generated PDF chunks
    """
    input_path = Path(input_path)
    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")
    
    output_dir = Path("utils/output")
    output_dir.mkdir(exist_ok=True)
    
    # Read the original PDF
    reader = PdfReader(str(input_path))
    total_pages = len(reader.pages)
    
    print(f"📖 Processing PDF: {input_path.name}")
    print(f"📄 Total pages: {total_pages}")
    print(f"📏 Original size: {get_file_size_mb(input_path):.1f} MB")
    print(f"🎯 Target max size: {max_size_mb} MB per chunk")
    print("-" * 50)
    
    output_files = []
    current_chunk = 1
    start_page = 0
    
    while start_page < total_pages:
        writer = PdfWriter()
        temp_file = None
        end_page = start_page
        
        # Add pages one by one until we hit the size limit
        for page_num in range(start_page, total_pages):
            writer.add_page(reader.pages[page_num])
            
            # Create temporary file to check size
            with tempfile.NamedTemporaryFile(suffix='.pdf', delete=False) as temp_file:
                writer.write(temp_file)
                temp_file.flush()
                current_size = get_file_size_mb(temp_file.name)
            
            # Clean up temp file
            if temp_file:
                os.unlink(temp_file.name)
            
            # If we exceed the size limit and we have at least one page, break
            if current_size > max_size_mb and page_num > start_page:
                end_page = page_num - 1
                # Remove the last page that pushed us over the limit
                writer = PdfWriter()
                for p in range(start_page, end_page + 1):
                    writer.add_page(reader.pages[p])
                break
            else:
                end_page = page_num
        
        # Generate output filename
        base_name = input_path.stem
        chunk_filename = f"{base_name}_chunk_{current_chunk:02d}_pages_{start_page + 1}-{end_page + 1}.pdf"
        output_path = output_dir / chunk_filename
        
        # Write the chunk
        with open(output_path, 'wb') as output_file:
            writer.write(output_file)
        
        chunk_size = get_file_size_mb(output_path)
        print(f"✅ Chunk {current_chunk}: {chunk_filename}")
        print(f"   📄 Pages {start_page + 1}-{end_page + 1} ({end_page - start_page + 1} pages)")
        print(f"   📏 Size: {chunk_size:.1f} MB")
        
        output_files.append(str(output_path))
        
        # Move to next chunk
        start_page = end_page + 1
        current_chunk += 1
        
        # Safety check to avoid infinite loops
        if start_page >= total_pages:
            break
    
    print("-" * 50)
    print(f"🎉 Successfully created {len(output_files)} chunks")
    print(f"📁 Output directory: {output_dir.absolute()}")
    
    return output_files


def main():
    parser = argparse.ArgumentParser(
        description="Split large PDF files into smaller chunks for AI processing"
    )
    parser.add_argument(
        "pdf_file", 
        help="Path to the PDF file to split"
    )
    parser.add_argument(
        "--max-size", 
        type=int, 
        default=30,
        help="Maximum size per chunk in MB (default: 30)"
    )
    
    args = parser.parse_args()
    
    try:
        output_files = split_pdf_by_size(args.pdf_file, args.max_size)
        
        print("\n🔄 Next Steps:")
        print("1. Upload each chunk to ChatGPT/Claude Desktop")
        print("2. Ask: 'Create flashcards from this DP-600 study material'")
        print("3. Copy the generated flashcards into your app")
        
        print(f"\n📋 Generated files:")
        for i, file_path in enumerate(output_files, 1):
            filename = Path(file_path).name
            size = get_file_size_mb(file_path)
            print(f"   {i}. {filename} ({size:.1f} MB)")
            
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()