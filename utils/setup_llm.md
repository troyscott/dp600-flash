# LLM Setup Guide for Best Quality Flashcards

## 🎯 Recommended: Local Ollama (Free + Private)

### 1. Install Ollama
```bash
# Windows: Download from https://ollama.ai
# Or use winget
winget install ollama

# macOS
brew install ollama

# Linux
curl -fsSL https://ollama.ai/install.sh | sh
```

### 2. Start Ollama Service
```bash
ollama serve
```

### 3. Install Recommended Models
```bash
# Best balance of quality/speed (3B params)
ollama pull llama3.2:3b

# Higher quality, slower (7B params)  
ollama pull qwen2.5:7b

# Lightweight option (1B params)
ollama pull llama3.2:1b
```

### 4. Test Installation
```bash
ollama list
# Should show your installed models

# Test generation
ollama run llama3.2:3b "Generate a test flashcard"
```

## 🌐 Alternative: Cloud LLMs (Paid but Highest Quality)

### OpenAI Setup
```python
# In hybrid_flashcard_generator.py, update CONFIG:
CONFIG = {
    "llm_provider": "openai",
    "model": "gpt-4o",  # or gpt-4o-mini for cheaper option
    "api_key": "your-openai-api-key"
}
```

### Anthropic Claude Setup  
```python
# In hybrid_flashcard_generator.py, update CONFIG:
CONFIG = {
    "llm_provider": "anthropic", 
    "model": "claude-3-5-sonnet-20241022",
    "api_key": "your-anthropic-api-key"
}
```

## 📊 Quality vs Cost Comparison

| Provider | Model | Quality | Speed | Cost | Privacy |
|----------|-------|---------|-------|------|---------|
| **Ollama (Local)** | llama3.2:3b | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | 🆓 FREE | 🔒 Private |
| Ollama | qwen2.5:7b | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | 🆓 FREE | 🔒 Private |
| OpenAI | gpt-4o | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ~$0.03/chunk | ☁️ Cloud |
| Anthropic | claude-3.5-sonnet | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ~$0.02/chunk | ☁️ Cloud |

## 🚀 Usage

### Default (Ollama)
```bash
cd utils
python hybrid_flashcard_generator.py
```

### With Cloud Provider
1. Edit `hybrid_flashcard_generator.py` CONFIG section
2. Add your API key
3. Run the script

## 🔧 Configuration Options

Edit the CONFIG section in `hybrid_flashcard_generator.py`:

```python
CONFIG = {
    "llm_provider": "ollama",     # ollama, openai, anthropic
    "model": "llama3.2:3b",       # model name
    "api_key": "",                # only for cloud providers
    "ollama_url": "http://localhost:11434",
    "max_cards_per_chunk": 12,    # cards per PDF chunk
    "min_content_length": 500     # skip short chunks
}
```

## 🎯 Recommended Workflow

1. **Start with Ollama** (free, private)
2. **Test with your PDF chunks**
3. **Upgrade to cloud LLM** if you need higher quality
4. **Compare results** and choose best option

The hybrid approach gives you the best of both worlds - smart preprocessing + LLM generation!