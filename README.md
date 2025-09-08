# DP-600 Study App

A comprehensive gamified flashcard app for Microsoft Fabric Analytics Engineer (DP-600) certification study with AI-powered content generation.

## 🚀 Features

- **5 Study Modes**: Topic Focus, Quick Study, Timed Practice, Full Study, Flash Cards
- **AI-Powered Content Generation**: Hybrid LLM + rule-based flashcard generation
- **Smart Content Analysis**: Auto-categorizes content into DP-600 exam objectives
- **PDF Processing Pipeline**: Split PDFs → Generate flashcards → Study immediately
- **Gamification**: Scoring, streaks, progress tracking with session management
- **Markdown-based Content**: Easy to create, edit, and manage flashcards
- **Responsive Design**: Works seamlessly on desktop and mobile
- **Local & Cloud LLM Support**: Use Ollama (free) or cloud APIs for best quality

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

### Adding New Flashcards - Complete Automated Workflow

**🏆 Recommended: Hybrid AI Generation (Best Quality)**
1. **Split PDFs**: `python utils/simple_pdf_splitter.py "path/to/study_guide.pdf"`
2. **Setup LLM** (one-time):
   ```bash
   # Install Ollama (free local LLM)
   winget install ollama
   ollama serve
   ollama pull llama3.2:3b
   ```
3. **Generate flashcards**: `python utils/hybrid_flashcard_generator.py`
4. **Load into app**: Visit `/admin/reload-flashcards`

**Alternative: Rule-based Generation (No LLM needed)**
1. Split PDFs as above
2. Run: `python utils/automated_flashcard_generator.py` 
3. Load into app as above

**Manual Creation**
1. Create `.md` files in `content/` subdirectories following the Q:/A: format
2. Separate cards with `---`
3. Reload at `/admin/reload-flashcards`

## 📚 Study Modes

- **Topic Focus**: Study specific DP-600 exam areas with scoring and streaks
- **Quick Study**: Stress-free review mode (5/10 cards, no scoring/timing)  
- **Timed Practice**: Exam simulation with time pressure (5/10/15 minutes)
- **Full Study**: Complete session through all available flashcards
- **Flash Cards**: Full gamified experience with correct/incorrect tracking

## 🛠️ Utilities

### AI Flashcard Generation
- **`hybrid_flashcard_generator.py`** - Best quality using LLM + rule-based analysis
- **`automated_flashcard_generator.py`** - Rule-based generation (no LLM required)
- **`claude_desktop_prompts.md`** - Manual prompt kit for Claude Desktop

### PDF Processing
- **`simple_pdf_splitter.py`** - Splits PDFs into 30-page chunks
- **`pdf_splitter.py`** - Size-based splitting (legacy)

### Setup Guides  
- **`setup_llm.md`** - Complete LLM setup guide (Ollama, OpenAI, Anthropic)

## Development

- **Reload flashcards**: Visit `/admin/reload-flashcards`
- **Debug**: Set `debug=True` in `app.py`
- **Add content**: Edit markdown files in `content/`

## 📁 Project Structure

```
dp600-flash/
├── app.py                          # Main Flask application
├── flashcard_loader.py             # Markdown parser & content loader
├── templates/                      # HTML templates (Jinja2)
│   ├── base.html                  # Base template
│   ├── home.html                  # Study mode selection
│   └── flashcard.html             # Card display & interaction
├── static/
│   └── style.css                  # Responsive CSS with markdown styling
├── content/                       # Flashcard markdown files
│   ├── 01-maintain-analytics-solution/
│   ├── 02-prepare-data/ 
│   └── 03-semantic-models/
├── utils/                         # AI generation & PDF processing utilities
│   ├── hybrid_flashcard_generator.py    # Best quality AI generation
│   ├── automated_flashcard_generator.py # Rule-based generation
│   ├── simple_pdf_splitter.py           # PDF chunking utility
│   ├── claude_desktop_prompts.md        # Manual prompt kit
│   └── setup_llm.md                     # LLM setup guide
├── requirements.txt               # Python dependencies
└── README.md                      # This documentation
```

## 🎯 Perfect for DP-600 Exam Prep

This app is specifically designed for the **Microsoft DP-600: Implementing Analytics Solutions Using Microsoft Fabric** certification exam, with content automatically organized by exam objectives and optimized study modes for effective learning and retention.