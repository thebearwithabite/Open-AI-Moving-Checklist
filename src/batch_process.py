#!/usr/bin/env python3
"""
Batch processor for multiple OpenAI export files
Processes all JSON files in a directory
"""

import sys
import os
from pathlib import Path
from persona_scraper import PersonaScraper


def batch_process(input_dir: str, output_dir: str = "output"):
    """
    Process all JSON files in input_dir and save to output_dir
    
    Args:
        input_dir: Directory containing OpenAI export JSON files
        output_dir: Directory to save extracted persona data
    """
    input_path = Path(input_dir)
    output_path = Path(output_dir)
    
    if not input_path.exists() or not input_path.is_dir():
        print(f"❌ Error: {input_dir} is not a valid directory")
        return False
    
    # Create output directory
    output_path.mkdir(parents=True, exist_ok=True)
    
    # Find all JSON files
    json_files = list(input_path.glob("*.json"))
    
    if not json_files:
        print(f"❌ No JSON files found in {input_dir}")
        return False
    
    print(f"🔍 Found {len(json_files)} JSON file(s) to process")
    print("="*60)
    
    successful = 0
    failed = 0
    
    for json_file in json_files:
        try:
            print(f"\n📄 Processing: {json_file.name}")
            scraper = PersonaScraper(str(json_file))
            scraper.load_and_scrape()
            
            # Create output filename
            output_file = output_path / f"persona_{json_file.stem}.json"
            scraper.export_to_json(str(output_file))
            
            successful += 1
            
        except Exception as e:
            print(f"❌ Failed to process {json_file.name}: {e}")
            failed += 1
    
    print("\n" + "="*60)
    print("BATCH PROCESSING COMPLETE")
    print("="*60)
    print(f"✅ Successfully processed: {successful} file(s)")
    if failed > 0:
        print(f"❌ Failed: {failed} file(s)")
    print(f"📁 Output directory: {output_path.absolute()}")
    print("="*60)
    
    return True


def main():
    """Main entry point for batch processor"""
    if len(sys.argv) < 2:
        print("Usage: python batch_process.py <input_directory> [output_directory]")
        print("\nExample:")
        print("  python batch_process.py ./exports/ ./processed/")
        print("  python batch_process.py ~/Downloads/openai_exports/")
        sys.exit(1)
    
    input_dir = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else "output"
    
    print("🚀 GPT-4o Batch Persona Data Processor")
    print("="*60)
    
    success = batch_process(input_dir, output_dir)
    
    if success:
        print("\n🎉 All done! Your persona data is now sovereign!")
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
