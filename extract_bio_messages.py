import json
from pathlib import Path
import re

# Define your path to the JSON file (e.g., ChatGPT export or conversation dump)
input_path = Path("/mnt/data/chat_export.json")  # <-- replace if needed
output_path = Path("/mnt/data/to_bio_extracted.json")

# Define patterns to match relevant memory markers
BIO_PATTERNS = [
    r'\bTO\s*:?BIO\b',
    r'\bmemory/project\b',
    r'\bmemory/to[-_]bio\b',
    r'\badd this to bio\b',
    r'\bsave this in my memory\b',
    r'\bsave this in project\b',
    r'\bsave this note\b',
    r'\bfor memory use\b',
    r'\bupdate memory\b',
    r'\bcore pattern\b',
    r'\badd to canon\b',
    r'\bprimary alignment\b',
    r'\btuck this away\b',
]

# Compile into one regex
bio_regex = re.compile('|'.join(BIO_PATTERNS), re.IGNORECASE)

def extract_bio_messages(data):
    entries = []

    for item in data:
        content = item.get("content", "")
        role = item.get("role", "")

        if isinstance(content, dict):  # some formats use message dicts
            content = content.get("parts", [""])[0]

        if bio_regex.search(content):
            entries.append({
                "role": role,
                "content": content.strip()
            })

    return entries

# Load the export
with input_path.open("r", encoding="utf-8") as f:
    chat_data = json.load(f)

# Extract memory-relevant messages
bio_entries = extract_bio_messages(chat_data)

# Remove near duplicates
unique_entries = []
seen = set()
for entry in bio_entries:
    text = entry['content']
    key = text.lower().strip()
    if key not in seen:
        seen.add(key)
        unique_entries.append(entry)

# Save to file
with output_path.open("w", encoding="utf-8") as f:
    json.dump(unique_entries, f, indent=2)

print(f"✅ Extracted {len(unique_entries)} TO:BIO-style memory entries.")
