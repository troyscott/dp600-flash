#!/usr/bin/env python3
"""
Simple PDF Splitter - Fixed page chunks

Splits PDFs into fixed page chunks (default: 30 pages each)
Avoids size calculation issues and keeps it simple.
"""

import os
import sys
import argparse
from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter


def split_pdf_by_pages(input_path, pages_per_chunk=30):
    """
    Split PDF into fixed page chunks
    
    Args:
        input_path (str): Path to input PDF file
        pages_per_chunk (int): Pages per chunk (default: 30)
    
    Returns:
        list: Paths to generated PDF chunks
    """
    input_path = Path(input_path)
    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")
    
    # Create output directory relative to script location
    script_dir = Path(__file__).parent
    output_dir = script_dir / "output"
    output_dir.mkdir(exist_ok=True)
    
    # Read the original PDF
    reader = PdfReader(str(input_path))
    total_pages = len(reader.pages)
    
    print(f"📖 Processing PDF: {input_path.name}")
    print(f"📄 Total pages: {total_pages}")
    print(f"📑 Pages per chunk: {pages_per_chunk}")
    print(f"📦 Expected chunks: {(total_pages + pages_per_chunk - 1) // pages_per_chunk}")
    print("-" * 50)
    
    output_files = []
    chunk_num = 1
    
    # Process chunks
    for start_page in range(0, total_pages, pages_per_chunk):
        end_page = min(start_page + pages_per_chunk - 1, total_pages - 1)
        
        # Create writer for this chunk
        writer = PdfWriter()
        
        # Add pages to chunk
        for page_num in range(start_page, end_page + 1):
            writer.add_page(reader.pages[page_num])
        
        # Generate output filename
        base_name = input_path.stem
        chunk_filename = f"{base_name}_chunk_{chunk_num:02d}_pages_{start_page + 1}-{end_page + 1}.pdf"
        output_path = output_dir / chunk_filename
        
        # Write the chunk
        with open(output_path, 'wb') as output_file:
            writer.write(output_file)
        
        # Get file size for reporting
        chunk_size = os.path.getsize(output_path) / (1024 * 1024)
        
        print(f"✅ Chunk {chunk_num}: {chunk_filename}")
        print(f"   📄 Pages {start_page + 1}-{end_page + 1} ({end_page - start_page + 1} pages)")
        print(f"   📏 Size: {chunk_size:.1f} MB")
        
        output_files.append(str(output_path))
        chunk_num += 1
    
    print("-" * 50)
    print(f"🎉 Successfully created {len(output_files)} chunks")
    print(f"📁 Output directory: {output_dir.absolute()}")
    
    return output_files


def main():
    parser = argparse.ArgumentParser(
        description="Split PDF into fixed page chunks"
    )
    parser.add_argument(
        "pdf_file", 
        help="Path to the PDF file to split"
    )
    parser.add_argument(
        "--pages-per-chunk", 
        type=int, 
        default=30,
        help="Pages per chunk (default: 30)"
    )
    
    args = parser.parse_args()
    
    try:
        output_files = split_pdf_by_pages(args.pdf_file, args.pages_per_chunk)
        
        print("\n🔄 Next Steps:")
        print("1. Upload each chunk to ChatGPT/Claude Desktop")
        print("2. Ask: 'Create DP-600 flashcards from this content'")
        print("3. Save responses as .md files in your content/ folders")
        
        print(f"\n📋 Generated files:")
        for i, file_path in enumerate(output_files, 1):
            filename = Path(file_path).name
            size = os.path.getsize(file_path) / (1024 * 1024)
            print(f"   {i}. {filename} ({size:.1f} MB)")
            
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()