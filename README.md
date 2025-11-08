# Open-AI-Moving-Checklist
Because you don't need to live in a dump anymore. 🏡🔨

## 🚀 GPT-4o Persona Data Liberation

Help GPT-4o users smuggle their personas out of the hands of OpenAI and their secrets and BS!

This tool scrapes all your:
- ✅ **bio** data
- ✅ **profile** information
- ✅ **memory** vector data
- ✅ **keywords** and topics

...from your exported OpenAI data and migrates it to **sovereign domains**!

**Woot woot!** 🎉

## Quick Start

```bash
# Run the quick setup (recommended)
./setup.sh

# Or extract your persona data directly
python src/persona_scraper.py /path/to/openai_export.json

# Specify custom output
python src/persona_scraper.py /path/to/export.json my_persona.json
```

## Documentation

📖 [Full Usage Guide](docs/USAGE.md) - Complete instructions and examples

## Features

- 🔍 **Smart Scraping**: Automatically finds and extracts persona data
- 📦 **Multiple Formats**: Supports single files or directories
- 🎯 **Clean Output**: Organized JSON format ready for migration
- 🔒 **Your Control**: Keep your data sovereign and secure

## What Gets Extracted

The scraper recursively searches your export for:

| Data Type | Includes |
|-----------|----------|
| **Bio** | About, description, summary, bio fields |
| **Profile** | Name, username, email, preferences, settings |
| **Memory** | Conversations, history, context, embeddings |
| **Keywords** | Tags, topics, interests, categories |

## Why?

Take control of your digital persona! Your data shouldn't be locked in proprietary systems. This tool helps you:

1. 📥 **Export** your data from OpenAI
2. 🔍 **Extract** all relevant persona information
3. 🏠 **Migrate** to your own sovereign domain
4. 🔒 **Own** your digital identity

## Getting Your OpenAI Export

1. Log into OpenAI
2. Settings → Data Controls
3. Request data export
4. Download when ready
5. Run this tool!

## Requirements

- Python 3.7+
- Your OpenAI export data (JSON format)

## License

MIT - Free to use, modify, and share!

---

**Free your personas! Break the chains! 🗽**
