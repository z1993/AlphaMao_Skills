# Note Meta Skill (知识萃取器) 🧠

> 从公域知识萃取方法论并封装为 Skill。通过 NotebookLM Deep Research 搜索优质内容，提炼工作流、原则、模板，自动生成标准化技能。

## ✨ 功能特点

- **知识收集**：通过 NotebookLM 自动搜索和收集优质内容
- **深度萃取**：提取 Workflow、Principles、Templates、Scripts
- **Skill 封装**：自动生成标准化的技能文件结构
- **混合输入**：支持 URL、本地文档、AI 自主搜索

## ⚠️ 前置要求

在使用此技能之前，您**必须**先安装以下依赖：

1. **NotebookLM Skill**：`notebooklm` 技能用于知识收集
2. **完成 NotebookLM 登录**：`notebooklm login`
3. **代理配置**（中国大陆必需）：
   ```powershell
   $env:HTTP_PROXY="http://127.0.0.1:7890"
   $env:HTTPS_PROXY="http://127.0.0.1:7890"
   ```

## 🚀 使用方法

触发技能：
> "帮我从这个博主的方法论创建一个 Skill"

或使用触发词：
- `/note-meta-skill`
- `从知识创建技能`
- `知识萃取`
- `元技能`

## 📖 工作流程

```
用户输入 (主题/URL/文档)
        ↓
  阶段1: 知识收集 (NotebookLM)
        ↓
  阶段2: 知识萃取 (Workflow/Principles/Templates)
        ↓
   ★ 用户确认 ★
        ↓
  阶段3: Skill 封装
        ↓
      交付 Skill
```

## 🙏 致谢

本技能依赖 [NotebookLM](https://notebooklm.google.com/) 进行知识收集和研究。

## 📄 许可证

MIT License
