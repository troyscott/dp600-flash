# DP-600 Study App

A gamified flashcard app for Microsoft Fabric Analytics Engineer (DP-600) certification study.

## Features

- **Multiple Study Modes**: Topic Focus, Timed Practice, Quick Study, Full Study
- **Gamification**: Scoring, streaks, progress tracking  
- **Markdown-based Content**: Easy to create and manage flashcards
- **PDF Splitter Utility**: Break down large study materials for AI processing
- **Responsive Design**: Works on desktop and mobile

## Quick Start

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the app:**
   ```bash
   python app.py
   ```

3. **Visit:** http://localhost:5000

## Flashcard Content System

Flashcards are stored as markdown files in the `content/` directory, organized by DP-600 exam objectives:

```
content/
├── 01-maintain-analytics-solution/
├── 02-prepare-data/
└── 03-semantic-models/
```

### Adding New Flashcards

**Option 1: Use Claude Desktop**
1. Use the PDF splitter utility: `python utils/pdf_splitter.py input/study_guide.pdf`
2. Upload chunks to Claude Desktop with this prompt:
   ```
   Create DP-600 flashcards using this format:
   
   **Q:** [question]
   **A:** [answer]
   
   Separate each card with ---
   ```
3. Save the output as `.md` files in appropriate `content/` subdirectories
4. Visit `/admin/reload-flashcards` to load new content

**Option 2: Manual Creation**
1. Create `.md` files in `content/` subdirectories
2. Follow the format in `content/README.md`
3. Use `---` separators between cards
4. Reload at `/admin/reload-flashcards`

## Study Modes

- **Topic Focus**: Study specific exam areas (Maintain, Prepare Data, Semantic Models)
- **Timed Practice**: Exam simulation with time pressure (5/10/15 minutes)  
- **Quick Study**: Stress-free review mode (5/10 cards, no scoring)
- **Full Study**: Complete session with all flashcards and scoring

## PDF Splitter Utility

Located in `utils/` - splits large PDF study materials into chunks for AI processing:

```bash
cd utils
pip install -r requirements.txt
python pdf_splitter.py input/large_study_guide.pdf
```

See `utils/README.md` for details.

## Development

- **Reload flashcards**: Visit `/admin/reload-flashcards`
- **Debug**: Set `debug=True` in `app.py`
- **Add content**: Edit markdown files in `content/`

## Project Structure

```
dp600-flash/
├── app.py                 # Main Flask application
├── flashcard_loader.py    # Markdown parser
├── templates/             # HTML templates  
├── static/               # CSS and assets
├── content/              # Flashcard markdown files
├── utils/                # PDF splitter utility
└── README.md             # This file
```