# Stanford Vibe Coding Course Skill

一个为 CS146S "The Modern Software Developer" (斯坦福大学 2025秋) 设计的 AI 学习辅导系统。

## 🎯 为什么用这个系统学习？

### 原版课程的价值

**CS146S 是目前最系统的 AI 开发课程之一**：
- 覆盖 AI 开发全链条：LLM → Agent → IDE → 安全 → 代码审查 → 运维
- MCP 协议深度讲解（目前最重要的 Agent 基础设施）
- 来自 Anthropic、Warp 等一线公司的最佳实践
- 8 个实践作业，动手验证学习成果

### 这个系统如何帮你更好地吸收

| 学习痛点 | 本系统解决方案 |
|---------|---------------|
| 英文材料读不动 | 45 篇专业翻译，术语保留英文 |
| 读完就忘 | 间隔复习闪卡 + 主动回忆问答 |
| 看不懂专业术语 | 随时 "解释 MCP" 获得通俗解释 |
| 不知道学习顺序 | 7天学习计划，按重要性排序 |
| 笔记散落各处 | Obsidian 结构化知识库，一处沉淀 |
| 学了不知道用 | 简化版作业，边学边练 |

> 💡 **核心理念**：不只是"翻译课程"，而是用科学方法（主动回忆、间隔复习）帮你真正掌握知识。

---

## 概述

这个 Skill 将 AI Coding Agent 转变为你的个人学习教练：

- 📚 **结构化学习**: 9周课程，45篇阅读材料，8个实践作业
- 🧠 **科学方法**: Zettelkasten 原子笔记 + 间隔复习闪卡
- 🇨🇳 **中文优先**: 所有内容提供中文翻译，技术术语保留英文
- 📊 **进度追踪**: 在 Obsidian Vault 中自动管理学习进度
- 💡 **新手友好**: 随时可以问 "解释 [术语]"，获得通俗解释

## 课程内容

| 周次 | 主题 | 核心内容 |
|------|------|----------|
| Week 1 | LLM入门 | Prompt Engineering 技术 |
| Week 2 | Agent架构 ⭐ | MCP协议 - 课程核心 |
| Week 3 | AI IDE | 上下文管理与工程 |
| Week 4 | Claude Code ⭐ | Coding Agent 实战 |
| Week 5 | 现代终端 | Warp 终端体验 |
| Week 6 | 安全 ⭐ | SAST/DAST/OWASP |
| Week 7 | 代码审查 | AI 辅助 Code Review |
| Week 8 | 运维 | SRE 与可观测性 |
| Week 9 | 未来 | 软件开发展望 |

## 安装

1. 将此文件夹复制到你的 Skills 目录:
   ```
   # Windows
   C:\Users\你的用户名\.gemini\antigravity\skills\stanford-vibe-coding-course\
   
   # macOS/Linux
   ~/.gemini/antigravity/skills/stanford-vibe-coding-course/
   ```

2. 创建或准备一个 Obsidian Vault（首次运行时会询问路径）

3. 安装 Obsidian 插件 (推荐):
   - [Spaced Repetition](https://github.com/st3v3nmw/obsidian-spaced-repetition) - 闪卡复习

## 使用方法

### 开始学习

```
学习 Week 2
```

系统会：
1. 读取你的当前进度
2. 显示本周内容（必读/选读）
3. 逐篇引导学习

### 核心命令

| 命令 | 作用 |
|------|------|
| `开始学习` | 首次启动，选择学习模式 |
| `学习 Week X` | 学习指定周次 |
| `读 [材料名]` | 阅读指定材料 |
| `解释 [术语]` | 获得通俗解释 |
| `读完了` | 完成阅读，进入问答环节 |
| `做作业` | 查看本周作业 |
| `交作业` | 提交作业获得评价 |
| `完成 Week X` | 生成定制化复习闪卡 |
| `我的进度` | 查看学习进度 |

### 学习流程

```
选择材料 → 阅读翻译 → 解释疑问 → 回答问题 → 生成笔记 → 周末生成定制闪卡
```

## 外部链接说明

⚠️ **部分内容需要访问原链接**

本 Skill 提供了 45 篇阅读材料的中文翻译，但以下类型内容无法完全在翻译中呈现：

- **GitHub 代码库**: 如 MCP Server 实现示例、Awesome Claude Agents
- **工具教程**: 如 Warp University 需要实际安装操作
- **动态内容**: 如 OWASP Top Ten 会定期更新

翻译提供核心概念和结构参考，完整学习需访问原链接。在 `course-content.md` 中标记为 🔗需访问原链接 的材料会在学习时提示。

## 文件结构

```
stanford-vibe-coding-course/
├── SKILL.md              # 主指令 (v1.0.0)
├── README.md             # 项目说明
├── CHANGELOG.md          # 版本记录
├── PROGRESS.md           # 开发进度
├── references/
│   ├── course-content.md      # 课程内容
│   ├── content-audit.md       # 内容分类审核
│   ├── why-this-matters.md    # 前置解释
│   ├── learning-methodology.md # 学习方法论
│   └── assignments-guide.md   # 简化作业指南
├── templates/
│   └── ...
└── translations/         # 45篇预翻译阅读材料
    └── weekX_XX_xxx.md
```

## 依赖

- **必需**: 
  - Claude Code (或其他支持 Skills 的 AI IDE)
  - Obsidian (存储笔记)
  
- **推荐**:
  - Obsidian Spaced Repetition 插件

## 贡献

欢迎提交 Issue 和 PR！

## 许可证

MIT License

## 致谢

本项目基于斯坦福大学 CS146S 课程的公开材料构建。感谢：

- **斯坦福大学 CS146S 课程团队** — 提供了系统化的 AI 开发课程框架
- **Mihail Eric** — 课程设计者，开放了高质量的学习资源
- **各阅读材料原作者** — 来自 Anthropic、Warp、OWASP 等组织的技术专家
- **Model Context Protocol 团队** — MCP 协议文档和示例

这是一个学习辅助工具，所有原始内容的版权归原作者所有。

## 相关链接

- [CS146S 官方课程](https://explorecourses.stanford.edu/search?view=catalog&filter-coursestatus-Active=on&q=CS%20146S)
- [课程作业仓库](https://github.com/mihail911/modern-software-dev-assignments)
