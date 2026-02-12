# Market Sizing Skill 📊

AI 驱动的市场规模测算工具，支持 Fermi 分解、Monte Carlo 模拟和自动化报告生成。

## 功能特点

- **5 种 Fermi 分解模式** — 人口基数法、机构基数法、替代法、价值链法、价值基础法
- **咨询级深度分解** — 3-5 层细分示例，含供给侧交叉验证和 Sanity Check
- **Monte Carlo 模拟** — 支持 Triangular/Normal/Uniform/LogNormal 分布，输出置信区间
- **敏感性分析** — Tornado Chart 确定关键假设
- **行业特化模板** — SaaS、Marketplace、Consumer、B2B、Hardware
- **自动数据获取** — AkShare、FRED、World Bank 等 6 大数据源
- **完整案例库** — 科技 (AI 开发工具)、消费 (预制菜)、软件 (财务 SaaS)

## 快速开始

```
# 触发词
"估算 XX 市场规模"
"市场规模分析"
"TAM/SAM/SOM"
"market size"
```

## 安装依赖 (可选)

```bash
# 核心 (Fermi Calculator 无需外部依赖)
pip install numpy          # Monte Carlo 模拟

# 数据获取
pip install pandas akshare baostock yfinance pytrends

# 报告生成
pip install plotly openpyxl

# FRED 数据
pip install fredapi
# 设置 FRED_API_KEY 环境变量
```

> **注意**: 不安装任何依赖也可以使用核心 Fermi 分解功能，AI 会以纯 Prompt 模式运行。

## 文件结构

```
market-sizing/
├── SKILL.md                    # 技能定义 (触发、流程、规范)
├── references/
│   ├── methodology.md          # TAM/SAM/SOM 方法论
│   ├── fermi_patterns.md       # Fermi 分解模式 (含深度指南)
│   ├── industry_templates.md   # 行业特化模板
│   ├── presentation_guide.md   # 呈现策略 (投资人 vs 战略)
│   ├── data_sources.md         # 数据源使用指南
│   └── prompts.md              # 后续分析提示库
├── examples/
│   ├── tech_ai_dev_tools.md    # 案例: AI 开发工具
│   ├── consumer_prefab_food.md # 案例: 预制菜
│   └── software_finance_saas.md# 案例: 财务 SaaS
├── scripts/
│   ├── fermi_calculator.py     # Fermi 计算引擎
│   ├── monte_carlo.py          # Monte Carlo 模拟
│   ├── data_fetcher.py         # 数据 API 封装
│   └── report_generator.py     # 报告生成器
└── templates/
    ├── market_sizing_report.md # Markdown 模板
    └── market_sizing_template.xlsx
```

## License

MIT
