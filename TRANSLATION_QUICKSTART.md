# Quick Start: Translation Agent

## 🚀 Quick Usage

### Translate a README file

1. Go to **Actions** tab
2. Click **"Translate README to English"**
3. Click **"Run workflow"**
4. (Optional) Enter the file path and source language
5. Click **"Run workflow"** button

### Example: Translate Spanish README

```
source_file: README.es.md
source_language: es
```

The workflow will create: `README.es.en.md`

## 📁 What Gets Created

- `{filename}.en.md` - English translation of your README
- `translation_summary.txt` - Summary with translation details (temporary)

## 🔍 View Results

After the workflow completes:
1. Check the workflow run for logs
2. Download artifacts to see the translation
3. The translated file will be committed to the branch

## 💡 Tips

- Use `auto` for automatic language detection
- Works with any README file in the repository
- Can translate files in subdirectories
- Creates a new file (doesn't overwrite originals)

For full documentation, see [TRANSLATION_GUIDE.md](TRANSLATION_GUIDE.md)
