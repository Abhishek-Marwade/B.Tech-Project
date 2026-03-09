# Research Compass - Multi-Agent System

## Quick Start

### 1. Get Your Groq API Key (2 minutes, FREE)

1. Go to: https://console.groq.com/keys
2. Sign up (free)
3. Click "Create API Key"
4. Copy the key

### 2. Configure

Open `.env` file and paste your key:
```
GROQ_API_KEY=gsk_your_key_here
AI_PROVIDER=groq
DISABLE_AI=false
```

### 3. Run

```bash
python run.py
```

Open browser: http://localhost:5000

## Features

- 🔍 **Smart Search**: Finds relevant research papers
- 📝 **AI Summaries**: Extracts methodology, results, limitations
- 💬 **Q&A Chat**: Ask questions about papers
- 💾 **Smart Caching**: Instant results on repeat queries
- ⚡ **Fast**: Uses Groq's lightning-fast inference

## Tech Stack

- **Backend**: Flask + Python
- **AI**: Groq API (Llama 3.3 70B)
- **Search**: Springer API
- **Cache**: SQLite
- **Frontend**: Vanilla JS + Modern CSS

## Why Groq?

- ✅ Very high free tier limits
- ✅ Extremely fast (faster than Gemini)
- ✅ Production-ready
- ✅ Industry standard

## Troubleshooting

**"GROQ_API_KEY not found"**
- Make sure `.env` file exists
- Check the key is correct
- Restart the app

**Search works but summaries fail**
- Check Groq dashboard for quota
- Try setting `DISABLE_AI=true` to test search only
