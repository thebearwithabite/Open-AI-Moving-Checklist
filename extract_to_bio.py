#!/usr/bin/env python3
"""
extract_to_bio.py - Extract memory and TO:BIO content from ChatGPT JSON exports

This script parses ChatGPT JSON export files and extracts:
- memory/project content
- memory/to-bio content
- TO:BIO style notes from conversations

Produces a clean, deduplicated export for the Core Memory Stack.
"""

import json
import re
import argparse
from pathlib import Path
from typing import List, Dict, Set, Any
from collections import OrderedDict


class MemoryExtractor:
    """Extract and deduplicate memory and TO:BIO content from ChatGPT exports."""
    
    def __init__(self):
        self.memories: Set[str] = set()
        self.to_bio_items: Set[str] = set()
        self.projects: Set[str] = set()
        
        # Patterns to match TO:BIO style content
        self.to_bio_patterns = [
            re.compile(r'\bTO:BIO\s+(.+?)(?:\n|$)', re.IGNORECASE | re.MULTILINE),
            re.compile(r'\bmemory/to-bio\s*:\s*(.+?)(?:\n|$)', re.IGNORECASE | re.MULTILINE),
        ]
        
        # Patterns to match memory/project content
        self.project_patterns = [
            re.compile(r'\bmemory/project\s*:\s*(.+?)(?:\n|$)', re.IGNORECASE | re.MULTILINE),
            re.compile(r'\bPROJECT\s*:\s*(.+?)(?:\n|$)', re.IGNORECASE | re.MULTILINE),
        ]
    
    def extract_from_text(self, text: str) -> None:
        """Extract memory content from a text string."""
        if not text:
            return
        
        # Extract TO:BIO content
        for pattern in self.to_bio_patterns:
            matches = pattern.findall(text)
            for match in matches:
                cleaned = match.strip()
                # Filter out very short matches or common words that might be false positives
                if cleaned and len(cleaned) > 3 and cleaned.lower() not in ['content', 'parts']:
                    self.to_bio_items.add(cleaned)
        
        # Extract project content
        for pattern in self.project_patterns:
            matches = pattern.findall(text)
            for match in matches:
                cleaned = match.strip()
                if cleaned and len(cleaned) > 3:
                    self.projects.add(cleaned)
    
    def extract_from_message(self, message: Dict[str, Any]) -> None:
        """Extract memory content from a message object."""
        # Extract from message content
        if 'content' in message:
            content = message['content']
            if isinstance(content, str):
                self.extract_from_text(content)
            elif isinstance(content, dict):
                # Handle structured content
                if 'parts' in content:
                    for part in content['parts']:
                        if isinstance(part, str):
                            self.extract_from_text(part)
        
        # Check for metadata or other fields
        if 'metadata' in message:
            metadata = message['metadata']
            if isinstance(metadata, dict):
                # Extract from memory fields
                if 'memory' in metadata:
                    memory_data = metadata['memory']
                    if isinstance(memory_data, str):
                        self.memories.add(memory_data)
                    elif isinstance(memory_data, dict):
                        for key, value in memory_data.items():
                            if isinstance(value, str):
                                self.memories.add(f"{key}: {value}")
    
    def extract_from_conversation(self, conversation: Dict[str, Any]) -> None:
        """Extract memory content from a conversation object."""
        # Extract from conversation title
        if 'title' in conversation:
            self.extract_from_text(conversation['title'])
        
        # Extract from mapping structure (common in ChatGPT exports)
        if 'mapping' in conversation:
            for node_id, node_data in conversation['mapping'].items():
                if 'message' in node_data and node_data['message']:
                    self.extract_from_message(node_data['message'])
        
        # Extract from messages array (alternative structure)
        if 'messages' in conversation:
            for message in conversation['messages']:
                self.extract_from_message(message)
    
    def extract_from_file(self, filepath: Path) -> None:
        """Extract memory content from a JSON file."""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # Handle different JSON structures
            if isinstance(data, list):
                # Array of conversations
                for item in data:
                    if isinstance(item, dict):
                        self.extract_from_conversation(item)
            elif isinstance(data, dict):
                # Single conversation or wrapped structure
                if 'conversations' in data:
                    for conversation in data['conversations']:
                        self.extract_from_conversation(conversation)
                else:
                    # Assume it's a single conversation
                    self.extract_from_conversation(data)
        
        except json.JSONDecodeError as e:
            print(f"Error parsing JSON file {filepath}: {e}")
        except Exception as e:
            print(f"Error processing file {filepath}: {e}")
    
    def get_deduplicated_export(self) -> Dict[str, List[str]]:
        """Get deduplicated memory content organized by category."""
        return {
            'to_bio': sorted(list(self.to_bio_items)),
            'projects': sorted(list(self.projects)),
            'memories': sorted(list(self.memories))
        }
    
    def export_to_text(self) -> str:
        """Export memory content as formatted text."""
        output = []
        
        if self.to_bio_items:
            output.append("=== TO:BIO Content ===\n")
            for item in sorted(self.to_bio_items):
                output.append(f"- {item}")
            output.append("")
        
        if self.projects:
            output.append("=== Projects ===\n")
            for item in sorted(self.projects):
                output.append(f"- {item}")
            output.append("")
        
        if self.memories:
            output.append("=== Other Memories ===\n")
            for item in sorted(self.memories):
                output.append(f"- {item}")
            output.append("")
        
        return "\n".join(output)


def main():
    """Main function to run the memory extractor."""
    parser = argparse.ArgumentParser(
        description='Extract memory and TO:BIO content from ChatGPT JSON exports',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s conversations.json
  %(prog)s conversations.json -o output.txt
  %(prog)s *.json --format json
        """
    )
    
    parser.add_argument(
        'files',
        nargs='+',
        type=Path,
        help='JSON export file(s) to process'
    )
    
    parser.add_argument(
        '-o', '--output',
        type=Path,
        help='Output file (default: print to stdout)'
    )
    
    parser.add_argument(
        '-f', '--format',
        choices=['text', 'json'],
        default='text',
        help='Output format (default: text)'
    )
    
    args = parser.parse_args()
    
    # Create extractor and process files
    extractor = MemoryExtractor()
    
    for filepath in args.files:
        if not filepath.exists():
            print(f"Warning: File not found: {filepath}")
            continue
        
        print(f"Processing: {filepath}", flush=True)
        extractor.extract_from_file(filepath)
    
    # Generate output
    if args.format == 'json':
        output = json.dumps(extractor.get_deduplicated_export(), indent=2)
    else:
        output = extractor.export_to_text()
    
    # Write or print output
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(output)
        print(f"\nResults written to: {args.output}")
    else:
        print("\n" + "="*60)
        print(output)
    
    # Print summary
    total_items = len(extractor.to_bio_items) + len(extractor.projects) + len(extractor.memories)
    print(f"\nSummary:")
    print(f"  TO:BIO items: {len(extractor.to_bio_items)}")
    print(f"  Projects: {len(extractor.projects)}")
    print(f"  Other memories: {len(extractor.memories)}")
    print(f"  Total: {total_items}")


if __name__ == '__main__':
    main()
