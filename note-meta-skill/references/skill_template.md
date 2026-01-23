# Skill 输出模板

生成 Skill 时使用的标准模板结构。

---

## SKILL.md 模板

```markdown
---
name: [skill-name]
description: [动作] + [场景] + [触发词]。例如："指导写作流程，适用于需要结构化写作的场景。触发词：/写作助手, 写作技巧, 文章创作"
---

# [Skill 名称]

[一句话描述 Skill 的核心价值]

## 概述

[2-3 句话说明：
1. 这个 Skill 能帮你做什么？
2. 适用于什么场景？
3. 基于什么知识/方法论？]

## 工作流

[从萃取结果的 Workflow 生成，格式如下：]

### 步骤 1: [步骤名称]
[具体动作说明]

### 步骤 2: [步骤名称]
[具体动作说明]

...

## 核心原则

[从萃取结果的 Principles 生成，格式如下：]

### 原则 1: [原则名称]
- **内容**: ...
- **Why**: ...

### 原则 2: [原则名称]
- **内容**: ...
- **Why**: ...

## 参考资料

[链接到 references/ 目录下的文件]

- [principles.md](references/principles.md) - 详细方法论
- [templates.md](references/templates.md) - 可复用模板

## 示例

[提供 1-2 个具体使用场景]

**场景**: [描述用户需求]
**输入**: [用户提供什么]
**输出**: [Skill 产出什么]
```

---

## references/principles.md 模板

```markdown
# 核心原则详解

[从萃取结果的 Principles 深度展开]

## 原则 1: [原则名称]

### 内容
[详细说明]

### 为什么重要
[解释 Why]

### 如何应用
[具体操作指导]

### 常见误区
[需要避免的错误做法]

---

## 原则 2: [原则名称]
...
```

---

## references/templates.md 模板

```markdown
# 可复用模板

[从萃取结果的 Templates 整理]

## 模板 1: [模板名称]

**用途**: [说明这个模板用于什么场景]

**模板内容**:
```
[具体模板]
```

**使用说明**:
1. ...
2. ...

---

## 模板 2: [模板名称]
...

---

## 检查清单

[如有]

- [ ] 检查项 1
- [ ] 检查项 2
```

---

## scripts/ 目录（如有脚本）

如果萃取结果包含脚本，按以下结构组织：

```
scripts/
├── main.py          # 主脚本
├── utils.py         # 工具函数
└── README.md        # 脚本使用说明
```

**scripts/README.md 模板**:
```markdown
# 脚本使用说明

## 环境要求
- Python 3.x
- 依赖: `pip install ...`

## 使用方法
```bash
python scripts/main.py --input ... --output ...
```

## 参数说明
- `--input`: ...
- `--output`: ...
```

---

## 命名规范

| 元素 | 规范 | 示例 |
|------|------|------|
| **Skill 目录名** | 小写 + 连字符 | `writing-master` |
| **SKILL.md** | 固定大写 | `SKILL.md` |
| **references/** | 固定名称 | `references/` |
| **scripts/** | 固定名称 | `scripts/` |
| **文件名** | 小写 + 连字符 | `principles.md` |

---

## 质量检查清单

生成 Skill 后，确保：

- [ ] **Frontmatter 完整**：name, description 都已填写
- [ ] **description 包含触发词**：中英文触发词都有
- [ ] **Workflow 清晰**：步骤明确，可执行
- [ ] **Principles 有 Why**：不只是 What，还有为什么
- [ ] **references 链接正确**：所有链接可访问
- [ ] **示例具体**：有真实的输入/输出案例
