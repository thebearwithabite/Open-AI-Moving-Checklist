#!/bin/bash
# Quick setup script for GPT-4o Persona Data Scraper

echo "🚀 GPT-4o Persona Data Scraper - Quick Setup"
echo "============================================="
echo ""

# Check Python version
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python 3 is required but not installed."
    echo "Please install Python 3.7 or higher and try again."
    exit 1
fi

PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
echo "✓ Found Python $PYTHON_VERSION"

# Make scraper executable
chmod +x src/persona_scraper.py
echo "✓ Made scraper executable"

# Test with example data
echo ""
echo "Testing with example data..."
python3 src/persona_scraper.py data/examples/sample_openai_export.json /tmp/test_persona.json

if [ $? -eq 0 ]; then
    echo ""
    echo "============================================="
    echo "✅ Setup complete! You're ready to go!"
    echo "============================================="
    echo ""
    echo "Usage:"
    echo "  python3 src/persona_scraper.py <your_export.json> [output.json]"
    echo ""
    echo "Example:"
    echo "  python3 src/persona_scraper.py ~/Downloads/openai_export.json my_persona.json"
    echo ""
    echo "📖 See docs/USAGE.md for more information"
    echo ""
else
    echo ""
    echo "❌ Setup test failed. Please check the error messages above."
    exit 1
fi
