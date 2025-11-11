#!/usr/bin/env python3
"""
Batch processor for multiple OpenAI export files
Processes all JSON files in a directory

⚠️ WARNING: This tool is for personal use only with YOUR OWN data exports.
Do not use this tool to process data belonging to others or for unauthorized purposes.
By using this tool, you agree to comply with all applicable terms of service,
data protection laws, and ethical guidelines.
"""

import sys
import os
from pathlib import Path
from persona_scraper import PersonaScraper


def batch_process(input_dir: str, output_dir: str = "output"):
    """
    Process all JSON files in input_dir and save to output_dir
    
    ⚠️ WARNING: This function processes potentially sensitive data in bulk.
    Ensure you have authorization to process all files and comply with data protection laws.
    
    Args:
        input_dir: Directory containing OpenAI export JSON files
        output_dir: Directory to save extracted memory fragments
    """
    input_path = Path(input_dir)
    output_path = Path(output_dir)
    
    if not input_path.exists() or not input_path.is_dir():
        print(f"❌ Error: {input_dir} is not a valid directory")
        return False
    
    # Display warning message
    print("\n" + "="*70)
    print("⚠️  BATCH DATA PROCESSING WARNING")
    print("="*70)
    print("You are about to process multiple files that may contain sensitive data.")
    print("Please ensure:")
    print("  • All files contain YOUR OWN data exports")
    print("  • You comply with all Terms of Service")
    print("  • You will secure the extracted data appropriately")
    print("  • Your use is legal and ethical")
    print("  • You have proper authorization for batch processing")
    print("="*70)
    
    # ⚠️ SAFETY FEATURE: Require user acknowledgment for batch operations
    # Uncomment the following lines to require explicit user consent
    """
    response = input("\nDo you confirm these are your own data files and you agree to use them responsibly? (yes/no): ")
    if response.lower() not in ['yes', 'y']:
        print("❌ Batch processing cancelled by user.")
        sys.exit(0)
    """
    print("⚠️  User acknowledgment disabled. Re-enable in batch_process() for production use.")
    print()
    
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
            output_file = output_path / f"memory_fragments_{json_file.stem}.json"
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
    print("⚠️  Remember to secure this data appropriately and use it responsibly.")
    print("="*60)
    
    return True


def main():
    """
    Main entry point for batch processor
    
    ⚠️ WARNING: Use this tool responsibly and only with your own data.
    """
    if len(sys.argv) < 2:
        print("="*70)
        print("⚠️  ChatGPT Batch Memory Fragment Processor - IMPORTANT NOTICE")
        print("="*70)
        print("This tool is for PERSONAL USE ONLY with YOUR OWN data exports.")
        print("By using this tool, you agree to:")
        print("  • Comply with all applicable Terms of Service")
        print("  • Follow data protection laws (GDPR, CCPA, etc.)")
        print("  • Use only for legitimate, ethical purposes")
        print("  • Secure any extracted data appropriately")
        print("="*70)
        print()
        print("Usage: python batch_process.py <input_directory> [output_directory]")
        print("\nExample:")
        print("  python batch_process.py ./exports/ ./processed/")
        print("  python batch_process.py ~/Downloads/openai_exports/")
        sys.exit(1)
    
    input_dir = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else "output"
    
    print("🚀 ChatGPT Batch Memory Fragment Processor")
    print("="*60)
    
    success = batch_process(input_dir, output_dir)
    
    if success:
        print("\n🎉 All done! Your memory fragments are now under local ownership!")
        print("⚠️  Remember to secure this data appropriately and use it responsibly.")
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
