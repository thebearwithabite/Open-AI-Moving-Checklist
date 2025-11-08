#!/usr/bin/env python3
"""
Test script for extract_bio_messages.py
"""
import json
import sys
from pathlib import Path
import re

# Import the functions from the main script
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

def test_extraction():
    """Test the bio message extraction"""
    print("🧪 Testing bio message extraction...")
    
    # Load test data
    test_file = Path("test_chat_export.json")
    with test_file.open("r", encoding="utf-8") as f:
        chat_data = json.load(f)
    
    print(f"📥 Loaded {len(chat_data)} messages from test file")
    
    # Extract bio messages
    bio_entries = extract_bio_messages(chat_data)
    print(f"🔍 Found {len(bio_entries)} messages with bio markers")
    
    # Remove duplicates
    unique_entries = []
    seen = set()
    for entry in bio_entries:
        text = entry['content']
        key = text.lower().strip()
        if key not in seen:
            seen.add(key)
            unique_entries.append(entry)
    
    print(f"✨ After deduplication: {len(unique_entries)} unique entries")
    
    # Expected results
    expected_count = 4  # TO:BIO (once after dedup), memory/project, add this to bio, save this in my memory
    
    if len(unique_entries) == expected_count:
        print(f"✅ Test passed! Expected {expected_count} unique entries, got {len(unique_entries)}")
        
        # Print the extracted entries
        print("\n📋 Extracted entries:")
        for i, entry in enumerate(unique_entries, 1):
            print(f"\n{i}. Role: {entry['role']}")
            print(f"   Content: {entry['content'][:80]}...")
        
        return True
    else:
        print(f"❌ Test failed! Expected {expected_count} unique entries, got {len(unique_entries)}")
        print("\n📋 Extracted entries:")
        for i, entry in enumerate(unique_entries, 1):
            print(f"\n{i}. Role: {entry['role']}")
            print(f"   Content: {entry['content']}")
        return False

def test_pattern_matching():
    """Test that all patterns are recognized"""
    print("\n🧪 Testing pattern matching...")
    
    test_patterns = [
        "TO:BIO - test message",
        "TO BIO - test message",
        "memory/project - test",
        "memory/to-bio - test",
        "memory/to_bio - test",
        "add this to bio please",
        "save this in my memory",
        "save this in project",
        "save this note for later",
        "for memory use only",
        "update memory with this",
        "this is a core pattern",
        "add to canon",
        "primary alignment note",
        "tuck this away for later",
    ]
    
    matched = 0
    for pattern in test_patterns:
        if bio_regex.search(pattern):
            matched += 1
        else:
            print(f"❌ Pattern not matched: {pattern}")
    
    if matched == len(test_patterns):
        print(f"✅ All {len(test_patterns)} patterns matched correctly!")
        return True
    else:
        print(f"⚠️  Only {matched}/{len(test_patterns)} patterns matched")
        return False

if __name__ == "__main__":
    result1 = test_extraction()
    result2 = test_pattern_matching()
    
    if result1 and result2:
        print("\n🎉 All tests passed!")
        sys.exit(0)
    else:
        print("\n💥 Some tests failed")
        sys.exit(1)
