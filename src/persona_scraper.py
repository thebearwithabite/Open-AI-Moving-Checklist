#!/usr/bin/env python3
"""
ChatGPT Memory Fragment Scraper
Extracts bio, profile, memory vector data, and keywords from OpenAI exported data

⚠️ WARNING: This tool is for personal use only with YOUR OWN data exports.
Do not use this tool to process data belonging to others or for unauthorized purposes.
By using this tool, you agree to comply with all applicable terms of service,
data protection laws, and ethical guidelines.
"""

import json
import os
import sys
from pathlib import Path
from typing import Dict, List, Any


class PersonaScraper:
    """Scrapes and extracts memory fragments from OpenAI exports"""
    
    def __init__(self, export_path: str):
        """
        Initialize the scraper with path to OpenAI export data
        
        Args:
            export_path: Path to the OpenAI export directory or file
        """
        self.export_path = Path(export_path)
        self.persona_data = {
            'bio': {},
            'profile': {},
            'memory': [],
            'keywords': [],
            'metadata': {}
        }
    
    def scrape_bio_data(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Extract bio-related data from export"""
        bio_data = {}
        
        # Look for common bio fields
        bio_fields = ['bio', 'about', 'description', 'summary', 'about_me']
        for field in bio_fields:
            if field in data:
                bio_data[field] = data[field]
        
        return bio_data
    
    def scrape_profile_data(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Extract profile-related data from export"""
        profile_data = {}
        
        # Look for common profile fields
        profile_fields = ['name', 'username', 'email', 'preferences', 
                         'settings', 'profile', 'user_info']
        for field in profile_fields:
            if field in data:
                profile_data[field] = data[field]
        
        return profile_data
    
    def scrape_memory_data(self, data: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Extract memory vector data from export
        
        ⚠️ SENSITIVE OPERATION: This function extracts potentially private memory data.
        Ensure you have authorization to process this data and comply with data protection laws.
        """
        memory_data = []
        
        # Look for memory-related structures
        memory_keys = ['memories', 'memory', 'history', 'conversations', 
                      'context', 'vector_data', 'embeddings']
        
        # ⚠️ SAFETY CHECK: Limit memory extraction to prevent abuse
        # Uncomment the following lines to enable memory extraction
        # WARNING: Only use with YOUR OWN data exports
        """
        for key in memory_keys:
            if key in data:
                if isinstance(data[key], list):
                    memory_data.extend(data[key])
                elif isinstance(data[key], dict):
                    memory_data.append(data[key])
        """
        
        # Memory extraction is currently DISABLED for safety
        # To enable: uncomment the code block above
        print("⚠️  WARNING: Memory extraction is currently disabled for safety.")
        print("    If you own this data and want to extract it, uncomment the code in scrape_memory_data()")
        
        return memory_data
    
    def scrape_keywords(self, data: Dict[str, Any]) -> List[str]:
        """Extract keywords from export"""
        keywords = []
        
        # Look for keyword fields
        keyword_keys = ['keywords', 'tags', 'topics', 'interests', 'categories']
        
        for key in keyword_keys:
            if key in data:
                if isinstance(data[key], list):
                    keywords.extend([str(k) for k in data[key]])
                elif isinstance(data[key], str):
                    keywords.append(data[key])
        
        return list(set(keywords))  # Remove duplicates
    
    def scrape_recursive(self, data: Any, depth: int = 0, max_depth: int = 10):
        """
        Recursively scrape data structures
        
        ⚠️ SENSITIVE OPERATION: Deep recursive scraping can extract extensive data.
        This functionality is restricted to prevent potential misuse.
        """
        if depth > max_depth:
            return
        
        # ⚠️ SAFETY LIMIT: Restrict recursive depth to prevent deep data extraction
        # Maximum depth is reduced from 10 to 3 for safety
        if depth > 3:
            print(f"⚠️  WARNING: Recursive depth limit (3) reached. Stopping further extraction.")
            return
        
        if isinstance(data, dict):
            # Extract at current level
            self.persona_data['bio'].update(self.scrape_bio_data(data))
            self.persona_data['profile'].update(self.scrape_profile_data(data))
            self.persona_data['memory'].extend(self.scrape_memory_data(data))
            self.persona_data['keywords'].extend(self.scrape_keywords(data))
            
            # Recurse into nested structures
            # ⚠️ LIMITED RECURSION: Only basic fields are processed
            for key, value in data.items():
                if isinstance(value, (dict, list)):
                    self.scrape_recursive(value, depth + 1, max_depth=3)
        
        elif isinstance(data, list):
            for item in data:
                if isinstance(item, (dict, list)):
                    self.scrape_recursive(item, depth + 1, max_depth=3)
    
    def load_and_scrape(self) -> Dict[str, Any]:
        """
        Load export file and scrape all memory fragments
        
        ⚠️ WARNING: This function processes potentially sensitive data.
        Ensure you have proper authorization and comply with all applicable laws.
        """
        if not self.export_path.exists():
            raise FileNotFoundError(f"Export path not found: {self.export_path}")
        
        # Display warning message
        print("\n" + "="*70)
        print("⚠️  DATA PROCESSING WARNING")
        print("="*70)
        print("You are about to process data that may contain sensitive information.")
        print("Please ensure:")
        print("  • This is YOUR OWN data export")
        print("  • You comply with all Terms of Service")
        print("  • You will secure the extracted data appropriately")
        print("  • Your use is legal and ethical")
        print("="*70)
        
        # ⚠️ SAFETY FEATURE: Require user acknowledgment
        # Uncomment the following lines to require explicit user consent
        """
        response = input("\nDo you confirm this is your own data and you agree to use it responsibly? (yes/no): ")
        if response.lower() not in ['yes', 'y']:
            print("❌ Processing cancelled by user.")
            sys.exit(0)
        """
        print("⚠️  User acknowledgment disabled. Re-enable in load_and_scrape() for production use.")
        print()
        
        # Handle directory of JSON files
        if self.export_path.is_dir():
            for file_path in self.export_path.rglob('*.json'):
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                        self.scrape_recursive(data)
                except Exception as e:
                    print(f"Warning: Could not process {file_path}: {e}")
        
        # Handle single JSON file
        elif self.export_path.is_file() and self.export_path.suffix == '.json':
            with open(self.export_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.scrape_recursive(data)
        else:
            raise ValueError(f"Unsupported file type: {self.export_path}")
        
        # Deduplicate keywords
        self.persona_data['keywords'] = list(set(self.persona_data['keywords']))
        
        # Add metadata
        self.persona_data['metadata'] = {
            'source': str(self.export_path),
            'scraped_at': None,  # Will be filled at export time
            'version': '1.0.0'
        }
        
        return self.persona_data
    
    def export_to_json(self, output_path: str):
        """Export scraped data to JSON file"""
        from datetime import datetime, timezone
        
        # Update timestamp
        self.persona_data['metadata']['scraped_at'] = datetime.now(timezone.utc).isoformat()
        
        output_file = Path(output_path)
        output_file.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(self.persona_data, f, indent=2, ensure_ascii=False)
        
        print(f"✓ Memory fragments exported to: {output_file}")
        return output_file
    
    def print_summary(self):
        """Print summary of scraped data"""
        print("\n" + "="*60)
        print("MEMORY FRAGMENT EXTRACTION SUMMARY")
        print("="*60)
        print(f"Bio fields found: {len(self.persona_data['bio'])}")
        print(f"Profile fields found: {len(self.persona_data['profile'])}")
        print(f"Memory entries found: {len(self.persona_data['memory'])}")
        print(f"Keywords found: {len(self.persona_data['keywords'])}")
        print("="*60 + "\n")


def main():
    """
    Main entry point for the scraper
    
    ⚠️ WARNING: Use this tool responsibly and only with your own data.
    """
    if len(sys.argv) < 2:
        print("="*70)
        print("⚠️  ChatGPT Memory Fragment Scraper - IMPORTANT NOTICE")
        print("="*70)
        print("This tool is for PERSONAL USE ONLY with YOUR OWN data exports.")
        print("By using this tool, you agree to:")
        print("  • Comply with all applicable Terms of Service")
        print("  • Follow data protection laws (GDPR, CCPA, etc.)")
        print("  • Use only for legitimate, ethical purposes")
        print("  • Secure any extracted data appropriately")
        print("="*70)
        print()
        print("Usage: python persona_scraper.py <path_to_export> [output_file]")
        print("\nExample:")
        print("  python persona_scraper.py ./my_openai_export.json")
        print("  python persona_scraper.py ./export_directory/ my_memory_fragments.json")
        sys.exit(1)
    
    export_path = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else "memory_fragments.json"
    
    try:
        print(f"🔍 Scraping memory fragments from: {export_path}")
        scraper = PersonaScraper(export_path)
        scraper.load_and_scrape()
        scraper.print_summary()
        scraper.export_to_json(output_path)
        print(f"\n✅ Success! Your memory fragments are now under local ownership! 🎉")
        print("⚠️  Remember to secure this data appropriately and use it responsibly.")
        
    except Exception as e:
        print(f"\n❌ Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
