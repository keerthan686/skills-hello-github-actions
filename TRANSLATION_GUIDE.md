# README Translation Agent Guide

## Overview

This repository includes a GitHub Actions workflow that automatically translates README files from any language to English. The translation agent uses Google Translate API through the `deep-translator` Python library.

## Features

- 🌍 **Automatic Language Detection**: Automatically detects the source language
- 📝 **Multiple File Support**: Can translate any README file in the repository
- 🔄 **Manual & Automatic Triggers**: Run on-demand or automatically when README files change
- 📊 **Translation Summary**: Generates a summary report of the translation
- 🔀 **Pull Request Integration**: Can create PRs with translations on feature branches

## How to Use

### Method 1: Manual Workflow Dispatch

1. Go to the **Actions** tab in your GitHub repository
2. Select **"Translate README to English"** workflow from the left sidebar
3. Click **"Run workflow"** button
4. Configure the inputs:
   - **source_file**: Path to the README file (default: `README.md`)
   - **source_language**: Source language code (default: `auto` for auto-detection)
5. Click **"Run workflow"** to start the translation

### Method 2: Automatic on Push

The workflow automatically runs when:
- Any file matching `README*.md` is pushed to the repository
- Any file matching `**/*README*.md` (README files in subdirectories) is modified

### Method 3: Via API or CLI

You can trigger the workflow using GitHub CLI:

```bash
gh workflow run translate-readme.yml \
  -f source_file=README.md \
  -f source_language=auto
```

Or using the GitHub REST API:

```bash
curl -X POST \
  -H "Accept: application/vnd.github.v3+json" \
  -H "Authorization: token YOUR_TOKEN" \
  https://api.github.com/repos/OWNER/REPO/actions/workflows/translate-readme.yml/dispatches \
  -d '{"ref":"main","inputs":{"source_file":"README.md","source_language":"auto"}}'
```

## Supported Language Codes

Common language codes you can use for `source_language`:

- `auto` - Auto-detect (default)
- `es` - Spanish
- `fr` - French
- `de` - German
- `it` - Italian
- `pt` - Portuguese
- `ru` - Russian
- `ja` - Japanese
- `zh-CN` - Chinese (Simplified)
- `zh-TW` - Chinese (Traditional)
- `ko` - Korean
- `ar` - Arabic
- `hi` - Hindi
- `nl` - Dutch
- `pl` - Polish
- `tr` - Turkish
- `vi` - Vietnamese
- `th` - Thai

For a complete list of supported languages, see [Google Translate Languages](https://cloud.google.com/translate/docs/languages).

## Output

The workflow generates:

1. **Translated README**: A new file with `.en.md` extension (e.g., `README.en.md`)
2. **Translation Summary**: A `translation_summary.txt` file with details about the translation
3. **Artifacts**: Both files are uploaded as workflow artifacts for 30 days

## Example Workflows

### Example 1: Translate a Spanish README

```yaml
# Manually trigger with:
source_file: README.es.md
source_language: es
```

This will create `README.es.en.md` with the English translation.

### Example 2: Translate with Auto-detection

```yaml
# Manually trigger with:
source_file: README.md
source_language: auto
```

The agent will automatically detect the source language and translate to English.

### Example 3: Translate README in a Subdirectory

```yaml
# Manually trigger with:
source_file: docs/README.fr.md
source_language: fr
```

This will create `docs/README.fr.en.md` with the English translation.

## Requirements

The workflow requires:
- ✅ Python 3.11
- ✅ `deep-translator` library (automatically installed)
- ✅ Write permissions for `contents` and `pull-requests`

## Workflow Permissions

The workflow needs the following permissions (already configured):

```yaml
permissions:
  contents: write        # To commit translated files
  pull-requests: write   # To create PRs with translations
```

## Troubleshooting

### Translation Failed

If translation fails, check:
1. The source file exists and is readable
2. The file content is valid UTF-8
3. The workflow logs for specific error messages

### Long Content

For very long README files (>5000 characters), the translation is split into chunks automatically to avoid API limitations.

### Rate Limits

Google Translate may have rate limits. If you encounter issues:
- Wait a few minutes before retrying
- Consider translating smaller files
- Use manual triggers to control frequency

## Advanced Usage

### Custom Translation Script

If you need to customize the translation logic, you can modify the inline Python script in the workflow file at `.github/workflows/translate-readme.yml`.

### Multiple Languages

To translate to languages other than English, modify the `target_lang` parameter in the translation script:

```python
translator = GoogleTranslator(source=source_lang, target='es')  # Translate to Spanish
```

## Contributing

To improve the translation agent:

1. Fork the repository
2. Modify `.github/workflows/translate-readme.yml`
3. Test your changes
4. Submit a pull request

## License

This translation agent workflow is provided as-is under the same license as the repository (MIT License).

## Support

For issues or questions:
- Open an issue in this repository
- Check the workflow logs in the Actions tab
- Review the translation summary artifact for details
