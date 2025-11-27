#!/usr/bin/env python3
"""
generate_remember_phrases.py - Convert ChatGPT memory export JSON into Copilot 'Remember that...' phrases
"""

import json
import argparse
from pathlib import Path

def generate_phrases(data):
    phrases = []
    
    # TO:BIO items
    for item in data.get("to_bio", []):
        phrases.append(f"Remember that {item}.")
    
    # Projects
    for project in data.get("projects", []):
        phrases.append(f"Remember that I am working on {project}.")
    
    # Other memories
    for mem in data.get("memories", []):
        phrases.append(f"Remember that {mem}.")
    
    return phrases

def main():
    parser = argparse.ArgumentParser(description="Generate Copilot memory phrases from JSON export")
    parser.add_argument("input", type=Path, help="Input JSON file (from extract_to_bio.py)")
    parser.add_argument("-o", "--output", type=Path, help="Output text file (default: print to stdout)")
    args = parser.parse_args()

    with open(args.input, "r", encoding="utf-8") as f:
        data = json.load(f)

    phrases = generate_phrases(data)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write("\n".join(phrases))
        print(f"Written {len(phrases)} phrases to {args.output}")
    else:
        print("\n".join(phrases))

if __name__ == "__main__":
    main()
