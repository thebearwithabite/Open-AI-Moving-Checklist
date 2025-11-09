# Example Data Files

This directory contains example input and output files to help you understand what the scraper does.

## Files

### `sample_openai_export.json`
Example of what your OpenAI export data might look like. This represents the structure you'll get from OpenAI when you request your data export.

### `expected_output.json`
Example of the scraped and organized output after running the memory fragment scraper on the sample export.

## Try It Yourself

Run the scraper on the sample data:

```bash
cd /path/to/Open-AI-Moving-Checklist
python src/persona_scraper.py data/examples/sample_openai_export.json test_output.json
```

Compare `test_output.json` with `expected_output.json` to see how the scraper works!

## Notes

- Your actual OpenAI export may have different field names
- The scraper is designed to handle various formats
- It recursively searches for relevant data fields
- All extracted data is deduplicated and organized
