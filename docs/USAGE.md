# ChatGPT Memory Fragment Scraper 🚀

## Overview

This tool helps ChatGPT users extract their memory fragments (bio, profile, memory vectors, keywords, etc.) from OpenAI exported data and migrate it to local ownership - taking control of your data!

**Because you don't need to live in that crazy neighborhood anymore. 🏡🔨**

## What It Does

The scraper extracts the following data from your OpenAI export:

- **Bio Data**: About sections, descriptions, summaries
- **Profile Data**: Name, username, preferences, settings
- **Memory Vectors**: Conversation history, context, embeddings
- **Keywords**: Tags, topics, interests, categories

All extracted data is saved in a clean JSON format that you can:
- Store under your own local ownership
- Import into other systems
- Backup and version control
- Keep private and secure

## Quick Start

### Prerequisites

- Python 3.7 or higher
- Your OpenAI export data (JSON format)

### Installation

1. Clone this repository:
```bash
git clone https://github.com/thebearwithabite/Open-AI-Moving-Checklist.git
cd Open-AI-Moving-Checklist
```

2. Make the scraper executable:
```bash
chmod +x src/persona_scraper.py
```

### Usage

#### Basic Usage

Extract data from a single JSON file:
```bash
python src/persona_scraper.py /path/to/openai_export.json
```

This will create `memory_fragments.json` in the current directory.

#### Specify Output File

```bash
python src/persona_scraper.py /path/to/export.json my_memory_fragments.json
```

#### Process Directory of Files

If your export contains multiple JSON files:
```bash
python src/persona_scraper.py /path/to/export_directory/ output.json
```

#### Batch Process Multiple Exports

Process multiple export files at once:
```bash
python src/batch_process.py /path/to/exports_directory/ /path/to/output_directory/
```

This will:
- Find all JSON files in the input directory
- Extract memory fragments from each one
- Save individual output files with `memory_fragments_` prefix
- Provide a summary of successful and failed extractions

## How to Get Your OpenAI Export

1. Log into your OpenAI account
2. Go to Settings → Data Controls
3. Request an export of your data
4. Download the export when ready
5. Use this tool to extract your memory fragments!

## Output Format

The scraper produces a JSON file with the following structure:

```json
{
  "bio": {
    "description": "Your bio data...",
    "about": "..."
  },
  "profile": {
    "name": "Your Name",
    "preferences": {...}
  },
  "memory": [
    {
      "conversation_id": "...",
      "context": "..."
    }
  ],
  "keywords": [
    "topic1",
    "topic2"
  ],
  "metadata": {
    "source": "/path/to/export",
    "scraped_at": "2024-01-01T00:00:00",
    "version": "1.0.0"
  }
}
```

## Examples

See the `data/examples/` directory for example input and output files.

## Taking Control of Your Data 🎯

Once you've extracted your data:

1. **Store it securely** on your own server or domain
2. **Version control it** with Git
3. **Backup regularly** to multiple locations
4. **Share selectively** - only with services you trust
5. **Keep it private** - it's YOUR data, YOUR choice

## Contributing

Contributions welcome! Feel free to:
- Report issues
- Suggest features
- Submit pull requests
- Share your migration stories

## License

MIT License - Use freely, modify as needed, share with others!

## Support

Having issues? Found a bug? Have suggestions?
- Open an issue on GitHub
- Check existing issues for solutions
- Contribute improvements

## Roadmap

- [ ] Support for more export formats
- [ ] Direct upload to local storage systems
- [ ] Encryption options for sensitive data
- [ ] Migration guides for specific platforms
- [ ] Automated backup scheduling

---

**Free your data! 🎉 Woot woot!**
