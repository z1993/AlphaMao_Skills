# Note Meta Skill (知识萃取器)

> 从公域知识萃取方法论并封装为 Skill。通过 NotebookLM Deep Research 搜索优质内容，提炼工作流、原则、模板，自动生成标准化技能。

## ✨ Features

- **知识收集**: 自动创建 NotebookLM 笔记本，支持 AI Deep Research 和自定义来源
- **深度萃取**: 结构化提问提取 Workflow（工作流）、Principles（原则）、Templates（模板）和 Scripts（脚本）
- **自动封装**: 将萃取结果自动转换为标准的 Antigravity Skill 结构
- **标准化输出**: 生成 SKILL.md、参考文档和脚本目录

## 📦 Installation

### Prerequisites

1. **Python**: Ensure Python 3.8+ is installed.
2. **Dependencies**: Install the required Python package:
   ```bash
   pip install notebooklm-py
   ```
3. **NotebookLM Skill**: Ensure the base `notebooklm` skill is installed.

### Install Skill

```bash
# Clone the repository
git clone https://github.com/z1993/note-meta-skill.git

# Copy to skills directory
cp -r note-meta-skill ~/.gemini/antigravity/skills/
```

## 🚀 Quick Start

1. **明确目标**: 告诉 AI 你想萃取什么主题（如 "写作方法论"）
2. **执行收集**: 技能会自动调用 NotebookLM 进行搜索和整理
3. **确认结果**: 检查提取出的工作流和原则
4. **获取技能**: 技能会自动生成新的 Skill 文件供你使用

## 🎯 Trigger Words

| Language | Trigger Phrases |
|----------|-----------------|
| 中文 | /note-meta-skill, 从知识创建技能, 知识萃取, 元技能 |
| English | note-meta-skill |

## ⚙️ Configuration

### Proxy Setup (Required for Mainland China)

If you are in a region requiring a proxy (e.g., Mainland China), verify your local proxy port (commonly 7890) and configure it:

```powershell
# Example: If your proxy is running on port 7890
$env:HTTP_PROXY="http://127.0.0.1:7890"
$env:HTTPS_PROXY="http://127.0.0.1:7890"
```

## 📂 Structure

```
note-meta-skill/
├── SKILL.md          # Main skill instructions
├── requirements.txt  # Python dependencies
├── references/       # Additional documentation
└── assets/           # Templates and resources
```

## 🙏 Acknowledgements

- Special thanks to **[notebooklm-py](https://pypi.org/project/notebooklm-py/)** for providing the essential Python interface to NotebookLM.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on how to submit pull requests.
