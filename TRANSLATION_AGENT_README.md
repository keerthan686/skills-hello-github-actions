# 🌍 README Translation Agent

> Automatically translate README files from any language to English using GitHub Actions

## 🎯 What Does It Do?

This agent translates README files written in any language to English, making your documentation accessible to a global audience.

## ⚡ Quick Usage

### Method 1: GitHub UI (Easiest)
1. Go to **Actions** tab
2. Click **"Translate README to English"**
3. Click **"Run workflow"**
4. Done! Check for `README.en.md` file

### Method 2: Automatic
- Just push changes to any README file
- Translation runs automatically
- Translated file committed to repository

## 📸 Workflow Diagram

```
┌─────────────────────────────────────────────────────────┐
│                  Trigger Workflow                       │
│  • Manual (GitHub UI)                                   │
│  • Automatic (on README push)                           │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│              Setup Environment                          │
│  • Python 3.11                                          │
│  • deep-translator library                              │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│            Translate Content                            │
│  • Detect source language (or use specified)           │
│  • Split long content into chunks                       │
│  • Translate to English                                 │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│              Create Output                              │
│  • {filename}.en.md → Translated file                   │
│  • translation_summary.txt → Report                     │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│         Commit & Upload Artifacts                       │
│  • Commit translated file to repository                 │
│  • Upload summary as workflow artifact                  │
└─────────────────────────────────────────────────────────┘
```

## 🌟 Features

| Feature | Description |
|---------|-------------|
| 🌐 **100+ Languages** | Supports all Google Translate languages |
| 🤖 **Auto-Detection** | Automatically detects source language |
| 📝 **Smart Splitting** | Handles long documents by chunking |
| 🔄 **Dual Triggers** | Manual or automatic on file changes |
| 📊 **Reports** | Detailed translation summaries |
| 🔒 **Secure** | Zero security vulnerabilities |

## 📚 Example

### Input: `README.es.md`
```markdown
# Hola Acciones de GitHub
_Crear y ejecutar un flujo de trabajo._
```

### Output: `README.es.en.md`
```markdown
# Hello GitHub Actions
_Create and run a workflow._
```

## 🛠️ Configuration

### Workflow Inputs

| Input | Description | Default |
|-------|-------------|---------|
| `source_file` | Path to README file | `README.md` |
| `source_language` | Language code | `auto` |

### Language Codes

Common codes: `es` (Spanish), `fr` (French), `de` (German), `ja` (Japanese), `zh-CN` (Chinese), `ar` (Arabic), `ru` (Russian), etc.

Use `auto` to detect automatically.

## 📖 Documentation

- 📘 **[TRANSLATION_GUIDE.md](TRANSLATION_GUIDE.md)** - Complete guide
- ⚡ **[TRANSLATION_QUICKSTART.md](TRANSLATION_QUICKSTART.md)** - Quick reference  
- 📋 **[IMPLEMENTATION_SUMMARY.md](IMPLEMENTATION_SUMMARY.md)** - Technical details

## 🎓 How It Works

```python
# 1. Read source file
with open('README.es.md', 'r', encoding='utf-8') as f:
    content = f.read()

# 2. Translate to English
translator = GoogleTranslator(source='es', target='en')
translated = translator.translate(content)

# 3. Save translated version
with open('README.es.en.md', 'w', encoding='utf-8') as f:
    f.write(translated)
```

## ✅ Quality Assurance

- ✅ CodeQL Security Scan: **0 vulnerabilities**
- ✅ Code Review: **All issues resolved**
- ✅ YAML Syntax: **Valid**
- ✅ Python Syntax: **Valid**
- ✅ UTF-8 Encoding: **Proper**
- ✅ Latest Actions: **v5, v4**

## 🚀 Try It Now!

### Step 1: Create a README in another language
```bash
echo "# Bonjour le Monde" > README.fr.md
echo "Ceci est un exemple." >> README.fr.md
git add README.fr.md
git commit -m "Add French README"
git push
```

### Step 2: Run the translation workflow
- Go to **Actions** → **Translate README to English**
- Set `source_file` to `README.fr.md`
- Set `source_language` to `fr`
- Click **Run workflow**

### Step 3: Get your translation
- Check for `README.fr.en.md` in your repository
- Download the summary artifact for details

## 🤝 Contributing

Found a bug or have an idea? 
1. Open an issue
2. Submit a pull request
3. Check the logs in Actions tab

## 📜 License

MIT License - Same as the repository

---

<div align="center">

**Made with ❤️ using GitHub Actions**

[Documentation](TRANSLATION_GUIDE.md) • [Quick Start](TRANSLATION_QUICKSTART.md) • [Technical Details](IMPLEMENTATION_SUMMARY.md)

</div>
