# Brain Dump 技能 🧠

一个为 Obsidian 打造的智能编排器，能将用户混乱的想法转化为结构化的笔记，自动分类为任务、灵感、思考和情绪。

## 🌟 功能特点

- **从大脑到仓库**：即时捕捉意识流输入。
- **自动分类**：自动将内容归类为“行动”、“灵感”、“思考”和“情绪”。
- **Obsidian 原生**：直接在您的仓库中生成格式精美的 Markdown 文件。
- **智能仪表盘**：自动创建并更新“Brain Dump 仪表盘”，可视化您的思维状态。

## ⚠️ 前置要求

在使用此技能之前，您**必须**先安装 **Obsidian Skills**：
[https://github.com/kepano/obsidian-skills](https://github.com/kepano/obsidian-skills)

请确保该基础环境已正确配置，否则本技能可能无法正常工作。

## 🚀 安装与设置

1. **安装技能**：
   将此仓库克隆到您的技能目录中。

2. **Obsidian 配置（关键步骤）**：
   本技能配合 Obsidian 的 **Dataview** 插件使用效果最佳，用于驱动仪表盘。
   
   - **安装 Dataview**：打开 Obsidian > 设置 > 第三方插件 > 浏览 > 搜索 "Dataview" > 安装并启用。
   - **文件路径**：技能默认配置保存路径为：`[请在此处填入您的Obsidian仓库路径]\Brain Dumps\`。 
     > **注意**：您**必须**编辑 `SKILL.md`，将路经修改为您实际的 Obsidian 仓库路径。

3. **仪表盘初始化**：
   首次运行技能时，它会自动在目标目录中创建一个 `Brain Dump Dashboard.md` 文件。该仪表盘使用 Dataview 查询来展示您最近的任务、想法和情绪趋势。

## 📖 使用方法

只需告诉 Agent：
> “Brain dump：我得去买牛奶，我对新 App 有个点子，今天感觉很棒。”

Agent 将会：
1. 解析您的输入。
2. 将其分类（行动、灵感、思考、情绪）。
3. 创建一个新的每日笔记（例如：`2026-01-23_BrainDump_Milk_App.md`）。
4. 更新您的仪表盘视图。

## 📂 输出结构

每次 Dump 都会创建如下结构的文件：

```markdown
# Brain Dump - 2026-01-23

## ✅ Actions
- [ ] 买牛奶 #todo

## 💡 Ideas
- 新 App 的概念 #idea

## 💭 Thoughts
- 对今天的反思 #thought

## ❤️ Emotions
- 感觉很棒 #emotion
```

## 🙏 致谢

特别感谢 **Obsidian Skills** 项目为我们提供了强大的基础：
[https://github.com/kepano/obsidian-skills](https://github.com/kepano/obsidian-skills)

同时也感谢 **Obsidian** 团队打造了如此强大的知识库工具。

## 🤝 贡献

欢迎提交贡献！请随意提交 Pull Request。

## 📄 许可证

MIT License
