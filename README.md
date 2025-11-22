# Open-AI-Moving-Checklist
Because you don’t need to live in a dump anymore. 🏡🔨

## 🧠 extract_to_bio.py

A Python script to parse ChatGPT JSON exports and extract memory and TO:BIO style content.

### Features

- Extracts `memory/project` content
- Extracts `memory/to-bio` content  
- Finds TO:BIO style notes buried in conversations
- Provides clean, deduplicated output
- Supports multiple JSON export formats
- Can process multiple files at once
- Outputs in text or JSON format

### Usage

```bash
# Basic usage - print to stdout
python3 extract_to_bio.py conversations.json

# Save to file
python3 extract_to_bio.py conversations.json -o output.txt

# Process multiple files
python3 extract_to_bio.py file1.json file2.json file3.json

# Output as JSON
python3 extract_to_bio.py conversations.json --format json

# Get help
python3 extract_to_bio.py --help
```

### Output

The script produces a clean, deduplicated export organized into three categories:

- **TO:BIO Content** - Personal information and preferences
- **Projects** - Project-related memories
- **Other Memories** - Additional memory content from metadata

This export can be edited and pruned into the Core Memory Stack.

### Supported JSON Formats

The script handles various ChatGPT export formats:
- Single conversation objects
- Arrays of conversations
- Conversations with `mapping` structure
- Conversations with `messages` array
- Metadata-embedded memories
