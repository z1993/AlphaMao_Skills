---
name: note-meta-skill
description: 从公域知识萃取方法论并封装为 Skill。通过 NotebookLM Deep Research 搜索优质内容，提炼工作流、原则、模板，自动生成标准化技能。触发词：/note-meta-skill, 从知识创建技能, 知识萃取, 元技能
---

# Note Meta Skill (知识萃取器)

从公域互联网或用户提供的文档中萃取优质知识，提炼出工作流、方法论、原则等核心内容，自动封装为标准化的 Skill。

## 前提条件

1. **NotebookLM Skill 已安装**：本技能依赖 `notebooklm` 技能进行知识收集
2. **Skill Creator 可用**：用于最终的技能封装
3. **已完成 NotebookLM 登录**：`notebooklm login`

### 代理配置（中国大陆必需）

在所有 `notebooklm` 命令前设置代理：

```powershell
$env:HTTP_PROXY="http://127.0.0.1:7890"
$env:HTTPS_PROXY="http://127.0.0.1:7890"
```

### 登录注意事项

⚠️ `notebooklm login` 完成后，**必须回到终端按 ENTER 键**才能保存认证状态。

### 常见问题速查

| 问题 | 解决方案 |
|------|----------|
| All connection attempts failed | 设置 `HTTP_PROXY`/`HTTPS_PROXY` |
| 登录后仍报 Auth expired | 登录后必须按 ENTER |
| TargetClosedError | 设置 `$env:NOTEBOOKLM_HOME="~/.notebooklm_fix"` 切换新目录 |

## 工作流

```
用户输入 (主题/URL/文档)
        ↓
  阶段1: 知识收集
        ↓
  阶段2: 知识萃取
        ↓
   ★ 确认点 ★
        ↓
  阶段3: Skill 封装
        ↓
      交付 Skill
```

---

## 阶段 1: 知识收集

### 步骤 1.1: 明确目标
询问用户：
- **主题**："你想从哪个领域/主题萃取知识？"
- **来源**："你有现成的文档/URL 吗？还是需要 AI 帮你搜索？"
- **期望输出**："你希望生成什么类型的 Skill？（工作流指导 / 方法论参考 / 自动化脚本）"

### 步骤 1.2: 创建 NotebookLM 笔记本
```bash
notebooklm create "知识萃取: [主题名称]"
```

### 步骤 1.3: 收集知识来源

**方式 A - AI 自主搜索（Deep Research）：**
```bash
notebooklm source add-research "[搜索查询]" --mode deep --no-wait
notebooklm research wait --import-all
```

**方式 B - 用户提供来源：**
```bash
# 添加 URL
notebooklm source add "https://..."

# 添加本地文件
notebooklm source add ./document.pdf
```

**方式 C - 混合模式（推荐）：**
先添加用户文档，再用 Deep Research 补充搜索。

### 步骤 1.4: 验证来源就绪
```bash
notebooklm source list --json
```
确认所有 source 的 status = READY 后继续。

---

## 阶段 2: 知识萃取

使用结构化提问从 NotebookLM 中萃取核心知识。

### 萃取维度

按顺序执行以下提问（完整 Prompt 见 [extraction_prompts.md](references/extraction_prompts.md)）：

| 维度 | 目的 | 核心问题 |
|------|------|----------|
| **Workflow** | 提取步骤化流程 | "这套方法的完整工作流是什么？每一步具体做什么？" |
| **Principles** | 提取核心原则/方法论 | "背后的核心原则是什么？为什么要这样做？" |
| **Templates** | 提取可复用模板 | "有没有可以直接复用的模板、框架或清单？" |
| **Scripts** | 探测是否有脚本 | "有没有涉及代码、脚本或自动化工具？" |

### 执行萃取
```bash
# 依次执行萃取提问
notebooklm ask "[Workflow 萃取 Prompt]" --json
notebooklm ask "[Principles 萃取 Prompt]" --json
notebooklm ask "[Templates 萃取 Prompt]" --json
notebooklm ask "[Scripts 萃取 Prompt]" --json
```

### 整理萃取结果

将所有萃取结果整理为结构化文档，格式如下：

```markdown
# 知识萃取报告: [主题名称]

## Workflow (工作流)
1. 步骤1: ...
2. 步骤2: ...

## Principles (核心原则)
- 原则1: ...（解释 Why）
- 原则2: ...

## Templates (模板)
[如有]

## Scripts (脚本)
[如有，提取代码；如无，标注"无"]
```

---

## ★ 确认点 ★

**暂停并向用户展示萃取结果**，确认：

1. 萃取内容是否准确、完整？
2. 有无需要补充或修改的地方？
3. 确认后继续进行 Skill 封装。

---

## 阶段 3: Skill 封装

### 步骤 3.1: 确定 Skill 元信息
根据萃取结果确定：
- **name**：小写 + 连字符，如 `writing-master`
- **description**：[动作] + [场景] + [触发词]
- **类型**：工作流指导 / 方法论参考 / 自动化脚本

### 步骤 3.2: 创建目录结构
```bash
mkdir -p ~/.gemini/antigravity/Skills/[skill-name]/references
```

### 步骤 3.3: 生成 SKILL.md

使用 [skill_template.md](references/skill_template.md) 作为基础模板，填入：

- **Frontmatter**：name, description
- **概述**：Skill 用途说明
- **工作流**：从 Workflow 萃取结果生成
- **核心原则**：从 Principles 萃取结果生成
- **模板/参考**：链接到 `references/` 目录
- **示例**：提供 1-2 个使用场景

### 步骤 3.4: 填充 references/

根据萃取内容创建：
- `principles.md`：详细方法论
- `templates.md`：可复用模板
- `[其他].md`：按需添加

### 步骤 3.5: 处理 Scripts（如有）

如果萃取结果包含脚本：
```bash
mkdir -p ~/.gemini/antigravity/Skills/[skill-name]/scripts
```
将脚本代码保存到 `scripts/` 目录。

---

## 输出清单

最终交付物：

```
[skill-name]/
├── SKILL.md              # 主技能文件
├── references/           # 参考资料
│   ├── principles.md     # 核心原则（如有）
│   └── templates.md      # 模板（如有）
└── scripts/              # 脚本（如有）
```

---

## 示例

**用户请求**："我想学习这位写作博主的方法，帮我做成一个 Skill"

**执行流程**：
1. 创建笔记本 `notebooklm create "知识萃取: 写作方法论"`
2. 添加博主文章 URL
3. Deep Research 补充搜索 "写作技巧 方法论"
4. 萃取 Workflow, Principles, Templates
5. 用户确认萃取结果
6. 生成 `writing-master/SKILL.md`
7. 交付技能

---

## 注意事项

- **质量优于速度**：宁可多轮萃取，不要漏掉关键内容
- **动态 Scripts**：不强制要求脚本，有则纳入，无则省略
- **语言风格**：生成的 Skill 应为中文，符合用户习惯
