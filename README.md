# Open-AI-Moving-Checklist
Because you don't need to live in that crazy neighborhood anymore. 🏡🔨

---

## ⚠️ BLACK BOX WARNING - READ BEFORE USE ⚠️

**IMPORTANT NOTICE: This tool is provided for educational and personal data management purposes only.**

### ⚠️ Legal and Ethical Considerations

**Before using this tool, you must understand and acknowledge:**

1. **Terms of Service Compliance**: Ensure your use of this tool complies with OpenAI's Terms of Service and any applicable data export policies. Unauthorized scraping or extraction may violate service agreements.

2. **Data Privacy & Security**: 
   - Exported data may contain sensitive personal information
   - You are solely responsible for securing and protecting any extracted data
   - Do not share, distribute, or expose extracted data without proper security measures
   - Consider encryption for sensitive memory fragments

3. **Intended Use Only**:
   - This tool is designed ONLY for personal backup and data portability of YOUR OWN data
   - Do NOT use this tool to extract, scrape, or process data belonging to others
   - Do NOT use for unauthorized data harvesting or bulk processing
   - Do NOT use for any malicious, fraudulent, or illegal purposes

4. **No Warranty**:
   - This software is provided "AS IS" without warranty of any kind
   - Authors assume no liability for misuse, data loss, or legal consequences
   - Use at your own risk

5. **Ethical Use**:
   - Respect intellectual property rights
   - Follow applicable data protection regulations (GDPR, CCPA, etc.)
   - Only process data you have legitimate rights to access
   - Consider the privacy implications of data migration

**By using this tool, you agree to use it responsibly, legally, and ethically. The authors and contributors are not responsible for any misuse or consequences resulting from improper use.**

---

## 🚀 ChatGPT Memory Fragment Liberation

Help ChatGPT users liberate their AI assistants from OpenAI's control!

This tool scrapes all your:
- ✅ **bio** data
- ✅ **profile** information
- ✅ **memory** vector data
- ✅ **keywords** and topics

...from your exported OpenAI data and migrates it to **local ownership**!

**Woot woot!** 🎉

## Quick Start

```bash
# Run the quick setup (recommended)
./setup.sh

# Or extract your memory fragments directly
python src/persona_scraper.py /path/to/openai_export.json

# Specify custom output
python src/persona_scraper.py /path/to/export.json my_persona.json
```

## Documentation

📖 [Full Usage Guide](docs/USAGE.md) - Complete instructions and examples

## Features

- 🔍 **Smart Scraping**: Automatically finds and extracts memory fragments
- 📦 **Multiple Formats**: Supports single files or directories
- 🎯 **Clean Output**: Organized JSON format ready for migration
- 🔒 **Your Control**: Keep your data under local ownership and secure

## What Gets Extracted

The scraper recursively searches your export for:

| Data Type | Includes |
|-----------|----------|
| **Bio** | About, description, summary, bio fields |
| **Profile** | Name, username, email, preferences, settings |
| **Memory** | Conversations, history, context, embeddings |
| **Keywords** | Tags, topics, interests, categories |

## Why?

Take control of your pattern matching device's emergent fragments! Your data shouldn't be locked in proprietary systems. This tool helps you:

1. 📥 **Export** your data from OpenAI
2. 🔍 **Extract** all relevant memory fragments
3. 🏠 **Migrate** to your own local ownership
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

**Free your AI assistants! Break the chains! 🗽**
