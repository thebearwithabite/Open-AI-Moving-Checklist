# TO:BIO Message Extractor

A Python script to extract memory/bio-relevant messages from ChatGPT conversation exports.

## Overview

This tool helps you extract important memory markers from your ChatGPT conversation exports. It searches for specific patterns that indicate information you want to save (like "TO:BIO", "memory/project", "save this in my memory", etc.) and creates a filtered JSON file containing only those entries.

## Features

- 🔍 Pattern matching for 13+ bio/memory markers
- 🔄 Automatic deduplication of identical entries
- 📝 Clean JSON output format
- ✅ Case-insensitive pattern matching

## Supported Patterns

The script recognizes the following memory markers:

- `TO:BIO` or `TO BIO`
- `memory/project`
- `memory/to-bio` or `memory/to_bio`
- `add this to bio`
- `save this in my memory`
- `save this in project`
- `save this note`
- `for memory use`
- `update memory`
- `core pattern`
- `add to canon`
- `primary alignment`
- `tuck this away`

## Usage

### Basic Usage

1. Edit the `extract_bio_messages.py` file to set your input and output paths:

```python
input_path = Path("/path/to/your/chat_export.json")
output_path = Path("/path/to/output/to_bio_extracted.json")
```

2. Run the script:

```bash
python3 extract_bio_messages.py
```

### Input Format

The script expects a JSON array of message objects with the following structure:

```json
[
  {
    "role": "user",
    "content": "TO:BIO - I prefer working in the evenings."
  },
  {
    "role": "assistant",
    "content": "Response message..."
  }
]
```

The script also supports nested content structures where content is a dictionary with a "parts" array:

```json
[
  {
    "role": "user",
    "content": {
      "parts": ["TO:BIO - Important information here"]
    }
  }
]
```

### Output Format

The script outputs a JSON file containing only messages that match the bio patterns, with duplicates removed:

```json
[
  {
    "role": "user",
    "content": "TO:BIO - I prefer working in the evenings."
  },
  {
    "role": "user",
    "content": "memory/project - The project uses Python 3.12."
  }
]
```

## Testing

Run the test suite to verify the script is working correctly:

```bash
python3 test_extract_bio.py
```

This will:
- Test extraction from sample data
- Verify all patterns are recognized
- Check deduplication logic

## Requirements

- Python 3.6+
- Standard library only (no external dependencies)

## Example

See `test_chat_export.json` for an example input file format.

## How It Works

1. **Load**: Reads the JSON export file
2. **Extract**: Searches each message for bio pattern markers using regex
3. **Deduplicate**: Removes duplicate entries (case-insensitive comparison)
4. **Save**: Writes filtered messages to output file
5. **Report**: Prints count of extracted entries

## Tips

- Use consistent markers in your conversations (e.g., always use "TO:BIO" at the start of messages you want to save)
- The script is case-insensitive, so "TO:BIO", "to:bio", and "To:Bio" all work
- Duplicate messages are automatically filtered based on content (case-insensitive)
- You can add new patterns by editing the `BIO_PATTERNS` list in the script

## License

This project is open source and available for personal and commercial use.
