#!/usr/bin/env python3
"""
Test script for the translation functionality
"""
import sys
import os
from deep_translator import GoogleTranslator

def translate_text(text, source_lang='auto', target_lang='en'):
    """Translate text to English using deep-translator"""
    try:
        translator = GoogleTranslator(source=source_lang, target=target_lang)
        # Split text into chunks if it's too long (Google Translate has a limit)
        max_length = 4500
        if len(text) <= max_length:
            return translator.translate(text)

        # Split by paragraphs and translate each
        paragraphs = text.split('\n\n')
        translated_paragraphs = []

        for para in paragraphs:
            if len(para) <= max_length:
                translated_paragraphs.append(translator.translate(para))
            else:
                # Split long paragraphs by newlines (for markdown structure)
                lines = para.split('\n')
                translated_lines = []
                for line in lines:
                    if line.strip():
                        translated_lines.append(translator.translate(line))
                    else:
                        translated_lines.append('')
                translated_paragraphs.append('\n'.join(translated_lines))

        return '\n\n'.join(translated_paragraphs)
    except Exception as e:
        print(f"Translation error: {e}")
        return text

def main():
    source_file = sys.argv[1] if len(sys.argv) > 1 else 'README.md'
    source_lang = sys.argv[2] if len(sys.argv) > 2 else 'auto'

    if not os.path.exists(source_file):
        print(f"Error: File {source_file} not found")
        sys.exit(1)

    print(f"Reading {source_file}...")
    with open(source_file, 'r', encoding='utf-8') as f:
        content = f.read()

    print(f"Translating from {source_lang} to English...")
    translated_content = translate_text(content, source_lang, 'en')

    # Create output filename
    base_name = os.path.basename(source_file)
    name_parts = os.path.splitext(base_name)
    output_file = f"{name_parts[0]}.en{name_parts[1]}"

    print(f"Writing translated content to {output_file}...")
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(translated_content)

    print(f"Translation complete! Output saved to {output_file}")

    # Also write a summary
    with open('translation_summary.txt', 'w', encoding='utf-8') as f:
        f.write(f"Source file: {source_file}\n")
        f.write(f"Source language: {source_lang}\n")
        f.write(f"Output file: {output_file}\n")
        f.write(f"Original size: {len(content)} characters\n")
        f.write(f"Translated size: {len(translated_content)} characters\n")

    # Write output file for shell script parsing (machine-readable)
    with open('.translation_output.txt', 'w', encoding='utf-8') as f:
        f.write(output_file)

if __name__ == '__main__':
    main()
