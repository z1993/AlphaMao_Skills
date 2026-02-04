# Investment Committee 🏛️

> 多 Agent 对抗式投资委员会 - 由三位传奇投资人风格的 AI 专家进行独立审查和辩论

[![Made with Antigravity](https://img.shields.io/badge/Made%20with-Antigravity-blue)](https://github.com/anthropics/anthropic-cookbook)

## ✨ 功能特点

- 🎭 **三位顶级投资人视角**：巴菲特（价值派）、木头姐（成长派）、德肯米勒（宏观派）
- ⚔️ **物理隔离的独立思考**：每个 Agent 是独立的 Gemini API 调用，避免"群体思维"
- 📊 **实时宏观数据注入**：自动抓取美债收益率、美元指数、VIX 等数据
- 🗳️ **投票决议机制**：多轮辩论后自动提取投票并生成最终决议

## ⚠️ 前置要求

| 依赖 | 说明 |
|------|------|
| **stock-research** (推荐) | 用于自动生成投资研报，作为本 skill 的输入 |
| **Gemini API Key** | 获取地址：[Google AI Studio](https://aistudio.google.com/app/apikey) |
| **代理 (中国大陆)** | 需要科学上网访问 Google API |

## 🔗 与 stock-research 的联动

```
典型工作流:
┌─────────────────┐      ┌──────────────────────┐
│  stock-research │ ───► │ investment-committee │
│  生成投资研报   │      │    多角度评审决议    │
└─────────────────┘      └──────────────────────┘
```

1. **先用 stock-research** 对目标公司进行深度研究，生成结构化研报
2. **再用 investment-committee** 让三位专家评审研报，形成投资决议

## 📦 安装

```bash
# 复制到 skills 目录
cp -r investment-committee ~/.gemini/antigravity/skills/

# 安装 Python 依赖
pip install -r ~/.gemini/antigravity/skills/investment-committee/requirements.txt
```

## 🚀 快速开始

```bash
# Windows PowerShell
$env:GEMINI_API_KEY='<YOUR_API_KEY>'
$env:HTTP_PROXY='http://127.0.0.1:<PORT>'  # 可选，根据你的代理配置

# 运行
python scripts/run_committee.py <path_to_report.md> --rounds 3 --output ./output
```

或直接对话触发：
> "用投委会评审这份研报"
> "让巴菲特、木头姐、德肯米勒辩论一下"

## 🎯 触发词

| 语言 | 触发短语 |
|------|----------|
| 中文 | 投委会评审、投资委员会、召开投委会 |
| English | investment committee, evaluate investment |

## 📂 项目结构

```
investment-committee/
├── SKILL.md              # 核心技能说明
├── TROUBLESHOOTING.md    # 常见问题排查
├── requirements.txt      # Python 依赖
├── scripts/
│   └── run_committee.py  # 主执行脚本
└── references/
    └── personas/         # 三位专家的深度人设
        ├── buffett.md
        ├── wood.md
        └── druckenmiller.md
```

## 📄 许可证

MIT License

---

Made with ❤️ using [Antigravity](https://github.com/anthropics/anthropic-cookbook)
