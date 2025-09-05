# PDF Splitter Utility

Split large DP-600 study PDFs into smaller chunks for AI processing to generate flashcards.

## Setup

1. Install requirements:
```bash
cd utils
pip install -r requirements.txt
```

## Usage

### Basic Usage
```bash
# Split PDF into 30MB chunks (default)
python pdf_splitter.py input/dp600_study_guide.pdf

# Custom size limit (25MB)
python pdf_splitter.py input/dp600_study_guide.pdf --max-size 25
```

### Folder Structure
```
utils/
├── input/          # Put your large PDF files here
├── output/         # Split chunks will be saved here  
├── pdf_splitter.py # Main script
├── requirements.txt
└── README.md
```

## Workflow

1. **Place PDF in input folder:**
   ```bash
   cp ~/Downloads/dp600_official_guide.pdf utils/input/
   ```

2. **Run the splitter:**
   ```bash
   python utils/pdf_splitter.py utils/input/dp600_official_guide.pdf
   ```

3. **Upload chunks to AI:**
   - Upload each chunk to ChatGPT/Claude Desktop
   - Prompt: "Create DP-600 flashcards from this study material. Format as question and answer pairs."

4. **Add flashcards to app:**
   - Copy generated flashcards to `app.py` FLASHCARDS list
   - Follow existing format with id, category, question, answer

## Example Output

```
📖 Processing PDF: dp600_study_guide.pdf
📄 Total pages: 247
📏 Original size: 89.3 MB
🎯 Target max size: 30 MB per chunk
--------------------------------------------------
✅ Chunk 1: dp600_study_guide_chunk_01_pages_1-89.pdf
   📄 Pages 1-89 (89 pages)
   📏 Size: 29.8 MB
   
✅ Chunk 2: dp600_study_guide_chunk_02_pages_90-167.pdf
   📄 Pages 90-167 (78 pages)
   📏 Size: 28.1 MB

✅ Chunk 3: dp600_study_guide_chunk_03_pages_168-247.pdf
   📄 Pages 168-247 (80 pages)
   📏 Size: 29.4 MB
--------------------------------------------------
🎉 Successfully created 3 chunks
```

Perfect for breaking down Microsoft's official DP-600 study guides and documentation!