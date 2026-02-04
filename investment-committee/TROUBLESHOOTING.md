# Investment Committee Skill - Troubleshooting Guide

本文档记录了在开发和运行本 Skill 过程中遇到的问题及其解决方案。

---

## 1. 网络连接问题 (Proxy)

### 问题描述
脚本运行时卡在 `[AGENT] 巴菲特 正在思考...`，无任何输出或错误。

### 原因
国内网络环境无法直接访问 Google Gemini API (`api.generativelanguage.googleapis.com`)。

### 解决方案
在脚本开头设置 HTTP_PROXY 和 HTTPS_PROXY 环境变量：
```python
# 替换为你的代理地址和端口
PROXY_URL = "http://127.0.0.1:<PORT>"  # 常见端口: 7890 (Clash), 1080 (v2ray)
os.environ["HTTP_PROXY"] = PROXY_URL
os.environ["HTTPS_PROXY"] = PROXY_URL
```

> **Agent 自动引导**: 如果运行时出现 `[INIT] No proxy configured` 消息，脚本会自动提示查阅本文档。

---

## 2. API 频率限制 (429 Resource Exhausted)

### 问题描述
运行过程中（通常在后面几轮）出现错误：
`[ERROR] 木头姐 生成失败: 429 RESOURCE_EXHAUSTED`

### 原因
Google Gemini API 对免费/试用层级有严格的 QPM (Queries Per Minute) 限制。多智能体高频对话容易触发此限制。

### 解决方案
已在 `run_committee.py` 中实现了**指数退避 (Exponential Backoff)** 重试机制：
1. 捕获 429 错误。
2. 等待 `2^attempt + random` 秒（例如 2s, 4s, 8s...）。
3. 最多重试 5 次。

如果仍然频繁遇到，建议增加 `time.sleep(1)` 的基础间隔，或升级 API Quota。

---

## 3. 文件无法在 Antigravity UI 中打开

### 问题描述
点击 Artifact 链接时出现 `Unable to resolve nonexistent file ...`。

### 原因
外部 python 脚本直接在磁盘创建的文件，Antigravity 系统无法感知其 Artifact ID，导致无法通过 UI 打开。

### 解决方案
**Stdout Capture 模式**:
1. 脚本不仅写入文件，还在执行结束时将文件内容打印到标准输出 (stdout)，包裹在 `<TAG_START>...<TAG_END>` 中。
2. Agent 读取 stdout 内容。
3. Agent 使用 `write_to_file(IsArtifact=True)` 工具*重新*写入该文件。
这意味着文件实际上被写了两次：一次由脚本写入（为了持久化），一次由 Agent 写入（为了注册 Artifact）。

---

## 4. Persona 脸谱化

### 问题描述
生成的辩论内容过于刻板，像是"扮演"而非"思考"。

### 原因
Persona MD 文件内容过于简略。

### 解决方案
使用 `references/personas/` 下的深度通用人设文件，包含思维内核、关注指标和 Few-shot 思考示例。

---

## 5. 宏观数据缺失

### 问题描述
Druckenmiller 的分析缺乏依据，只能泛泛而谈。

### 原因
LLM 的知识截止于训练时间，无法知道当下的市场数据（利率、VIX等）。

### 解决方案
在脚本启动时使用 `yfinance` 库抓取实时宏观数据，并作为 `Special Context` 注入给 Druckenmiller。
