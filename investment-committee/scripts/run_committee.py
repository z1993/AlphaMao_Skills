"""
Investment Committee - Google GenAI Implementation (V3)
========================================================
Features:
- Live Macro Data Injection (yfinance) for Druckenmiller
- External Deep Personas (Generic Investment Philosophy)
- Phase 1-3 Workflow (Review -> Debate -> Decision)
- Proxy Support
"""

import os
import sys
import time
import argparse
import re
import traceback
import random
from datetime import datetime
from pathlib import Path

# Force stdout to flush immediately
sys.stdout.reconfigure(line_buffering=True)

# --- PROXY CONFIGURATION ---
# 代理配置：从环境变量读取，不设置硬编码默认值
# 如遇网络问题，请参考 TROUBLESHOOTING.md 或设置 HTTP_PROXY 环境变量
PROXY_URL = os.environ.get("HTTP_PROXY") or os.environ.get("HTTPS_PROXY")
if PROXY_URL:
    os.environ["HTTP_PROXY"] = PROXY_URL
    os.environ["HTTPS_PROXY"] = PROXY_URL
    print(f"[INIT] Proxy configured: {PROXY_URL}", flush=True)
else:
    print("[INIT] No proxy configured. If you're in China, set HTTP_PROXY env var.", flush=True)
    print("[INIT] See TROUBLESHOOTING.md for details.", flush=True)

print("[INIT] Starting Investment Committee Script (V3)...", flush=True)

# --- IMPORTS ---
try:
    from google import genai
    from google.genai import types
    print(f"[INIT] Successfully imported google.genai", flush=True)
except ImportError as e:
    print(f"[ERROR] Failed to import google.genai: {e}", flush=True)
    print("[INFO] Trying to install: pip install google-genai", flush=True)
    os.system("pip install google-genai")
    from google import genai
    from google.genai import types

try:
    import pandas as pd
    import yfinance as yf
    print(f"[INIT] Successfully imported yfinance", flush=True)
except ImportError:
    print("[INFO] Installing yfinance...", flush=True)
    os.system("pip install yfinance")
    import yfinance as yf

# --- CONSTANTS ---
SKILL_DIR = Path(__file__).parent.parent
PERSONA_DIR = SKILL_DIR / "references" / "personas"
PERSONA_NAMES = ["巴菲特", "木头姐", "德肯米勒"]

# --- HELPER FUNCTIONS ---

def get_macro_data() -> str:
    """Fetch key macro indicators for Druckenmiller context."""
    print("[MACRO] Fetching live market data...", flush=True)
    try:
        tickers = {
            "^TNX": "10-Year Treasury Yield",
            "DX-Y.NYB": "US Dollar Index",
            "^VIX": "VIX Volatility Index",
            "SPY": "S&P 500 ETF",
            "QQQ": "Nasdaq 100 ETF"
        }
        
        # Fetch more data (50 days) to handle holidays/weekends and fill NA
        data = yf.download(list(tickers.keys()), period="3mo", interval="1d", progress=False)['Close']
        data = data.ffill()  # Forward fill missing data
        
        latest = data.iloc[-1]
        prev_month = data.iloc[-22] # Approx 1 month trading days
        
        lines = ["### 🌍 实时宏观快照 (Live Macro Snapshot)"]
        for symbol, name in tickers.items():
            if symbol not in latest: continue
            curr_val = latest[symbol]
            month_ago = prev_month[symbol]
            # Handle potential zero division or NaN
            if pd.isna(curr_val) or pd.isna(month_ago) or month_ago == 0:
                 lines.append(f"- **{name} ({symbol})**: N/A")
                 continue
                 
            change = ((curr_val - month_ago) / month_ago) * 100
            
            # Trend determination
            trend = "Flat"
            if change > 2: trend = "Up ↑"
            elif change < -2: trend = "Down ↓"
            
            # Specific formatting for yields and indices
            if symbol == "^TNX":
                val_str = f"{curr_val:.2f}%"
            else:
                val_str = f"{curr_val:.2f}"
                
            lines.append(f"- **{name} ({symbol})**: {val_str} (1-Month Trend: {change:+.1f}% {trend})")
            
        report = "\n".join(lines)
        print("[MACRO] Data fetched successfully.", flush=True)
        return report
    except Exception as e:
        print(f"[WARN] Failed to fetch macro data: {e}", flush=True)
        return "（宏观数据获取失败，请基于一般市场认知假设）"

def load_persona(name: str) -> str:
    """Load persona prompt from markdown file."""
    filename = {
        "巴菲特": "buffett.md",
        "木头姐": "wood.md",
        "德肯米勒": "druckenmiller.md"
    }.get(name)
    
    path = PERSONA_DIR / filename
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        return content
    else:
        return f"你是一位投资专家，名为{name}。"

def create_client(api_key):
    """Create GenAI client."""
    return genai.Client(api_key=api_key)

def generate_response(client, persona_name, persona_prompt, context, instruction, special_context="", max_tokens=1024):
    """Generate a response from one agent."""
    print(f"[AGENT] {persona_name} 正在思考...", flush=True)
    
    # Inject special context (e.g. macro data) if available
    context_section = f"【背景信息】\n{context[:10000]}"
    if special_context:
        context_section += f"\n\n【专属情报 (仅{persona_name}可见)】\n{special_context}"
    
    full_prompt = f"""
{persona_prompt}

---
{context_section}

---
【本轮任务】
{instruction}

请以 {persona_name} 的身份用中文回复（300-500字）：
"""
    
    max_retries = 5
    base_delay = 2

    for attempt in range(max_retries):
        try:
            response = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=full_prompt,
                config=types.GenerateContentConfig(
                    temperature=0.7,
                    max_output_tokens=max_tokens,
                )
            )
            result = response.text
            print(f"[AGENT] {persona_name} 完成回复 ({len(result)} 字符)", flush=True)
            return result
        except Exception as e:
            error_msg = str(e)
            if "429" in error_msg or "RESOURCE_EXHAUSTED" in error_msg:
                delay = (base_delay ** attempt) + random.uniform(0, 1)
                print(f"[WARN] {persona_name} hit rate limit (429). Retrying in {delay:.2f}s... (Attempt {attempt+1}/{max_retries})", flush=True)
                time.sleep(delay)
            else:
                print(f"[ERROR] {persona_name} 生成失败: {e}", flush=True)
                return f"[生成失败: {e}]"
    
    return f"[生成失败: 达到最大重试次数 ({max_retries})]"

def extract_vote(response_text: str) -> dict:
    """Extract vote and confidence."""
    vote = "未表态"
    confidence = 50
    
    vote_patterns = [
        (r"(强力)?(买入|建议买入|推荐买入|增持)", "买入"),
        (r"(明确)?(拒绝|卖出|减持|做空|不推荐|放弃)", "拒绝"),
        (r"(继续)?(观望|等待|观察|中性|持有)", "观望"),
    ]
    for pattern, vote_label in vote_patterns:
        if re.search(pattern, response_text):
            vote = vote_label
            break
            
    conf_match = re.search(r"置信度.*?(\d+)%?", response_text)
    if conf_match:
        confidence = int(conf_match.group(1))
    
    return {"vote": vote, "confidence": confidence}

def save_transcript(output_dir, transcript, votes, phase="debate"):
    """Save debate transcript to file."""
    transcript_path = os.path.join(output_dir, "debate_transcript.md")
    vote_summary = "\n".join([f"- {name}: {v['vote']} (置信度 {v['confidence']}%)" for name, v in votes.items()])
    
    with open(transcript_path, "w", encoding="utf-8") as f:
        f.write(f"# 投资委员会辩论记录\n")
        f.write(f"**生成时间**: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
        f.write(f"**阶段**: {phase}\n\n")
        f.write(f"## 当前投票状态\n{vote_summary}\n\n")
        f.write("---\n\n")
        f.write("\n\n".join(transcript))

def run_committee(report_path, rounds, output_dir, api_key):
    """Run the full process."""
    print(f"[COMMITTEE] 启动流程...", flush=True)
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    client = create_client(api_key)
    
    # 1. Fetch Macro Data
    macro_snapshot = get_macro_data()
    
    # 2. Read Report
    with open(report_path, "r", encoding="utf-8") as f:
        report_content = f.read()
    
    # 3. Load Personas
    personas = {name: load_persona(name) for name in PERSONA_NAMES}
    
    transcript = []
    votes = {name: {"vote": "未表态", "confidence": 50} for name in PERSONA_NAMES}
    
    # --- PHASE 1 & 2: DEBATE ---
    for round_idx in range(rounds):
        print(f"\n{'='*60}", flush=True)
        print(f"[PHASE 1-2] Round {round_idx + 1}/{rounds}", flush=True)
        print(f"{'='*60}", flush=True)
        
        for persona_name in PERSONA_NAMES:
            # Special Context for Druckenmiller
            special_ctx = macro_snapshot if persona_name == "德肯米勒" else ""
            
            context = f"【研究报告摘要】\n{report_content[:6000]}\n\n【之前的讨论】\n" + "\n".join(transcript[-6:])
            
            if round_idx == 0:
                instruction = """这是第一轮独立评审。请阅读研报，给出你对这家公司的独立初评。
回复末尾必须包含：'结论：[买入/拒绝/观望]' 和 '置信度：[0-100]%'。"""
            else:
                instruction = """请反驳其他委员的观点。引用他们的原话并指出谬误。
回复末尾必须包含更新后的：'结论：[买入/拒绝/观望]' 和 '置信度：[0-100]%'。"""
            
            response = generate_response(client, persona_name, personas[persona_name], context, instruction, special_context=special_ctx)
            
            votes[persona_name] = extract_vote(response)
            transcript.append(f"### {persona_name}\n{response}")
            save_transcript(output_dir, transcript, votes, phase="debate")
            time.sleep(1)

    # --- PHASE 3: DECISION ---
    print(f"\n{'='*60}\n[PHASE 3] 决议生成\n{'='*60}", flush=True)
    vote_summary = "\n".join([f"- {name}: {v['vote']} ({v['confidence']}%)" for name, v in votes.items()])
    
    today_str = datetime.now().strftime('%Y年%m月%d日')

    chairman_prompt = f"""作为投委会秘书，请根据以下信息撰写《投资委员会决议》：

【当前日期】
{today_str}

【投票结果】
{vote_summary}

【宏观背景】
{macro_snapshot}

【辩论记录】
{chr(10).join(transcript[-9:])}

要求：
1. 总结共识与分歧。
2. 结合宏观数据（如美债收益率、VIX）论证最终建议。
3. 给出明确的最终决定（买入/拒绝/观望）及触发条件。
用中文，300字左右。
"""
    decision = client.models.generate_content(
        model="gemini-2.0-flash", 
        contents=chairman_prompt,
        config=types.GenerateContentConfig(temperature=0.3)
    ).text
    
    # Format Macro Section for Final Report
    macro_section = f"## 附录：决策时的宏观环境\n{macro_snapshot}\n"
    
    today_str = datetime.now().strftime('%Y年%m月%d日')
    
    with open(os.path.join(output_dir, "final_decision.md"), "w", encoding="utf-8") as f:
        f.write("# 投资委员会最终决议\n")
        f.write(f"**日期**: {today_str}\n\n")
        f.write(f"## 投票\n{vote_summary}\n\n")
        f.write(f"## 决议\n{decision}\n\n")
        f.write(macro_section)
    
    transcript.append(f"---\n## 最终决议\n{decision}\n\n{macro_section}")
    save_transcript(output_dir, transcript, votes, phase="final")
    save_transcript(output_dir, transcript, votes, phase="final")
    print(f"[DONE] 完成！输出目录: {output_dir}", flush=True)

    # --- OUTPUT FOR AGENT CAPTURE ---
    # Print the full content of the decision file to stdout so the agent can capture it
    # and create a proper artifact without needing file permission workaround.
    print("\n<FINAL_DECISION_START>", flush=True)
    with open(os.path.join(output_dir, "final_decision.md"), "r", encoding="utf-8") as f:
        print(f.read(), flush=True)
    print("<FINAL_DECISION_END>", flush=True)

    print("\n<DEBATE_TRANSCRIPT_START>", flush=True)
    with open(os.path.join(output_dir, "debate_transcript.md"), "r", encoding="utf-8") as f:
        print(f.read(), flush=True)
    print("<DEBATE_TRANSCRIPT_END>", flush=True)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("report_path")
    parser.add_argument("--rounds", type=int, default=3)
    parser.add_argument("--output", default="./ic_output")
    args = parser.parse_args()
    
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("[ERROR] GEMINI_API_KEY missing")
        sys.exit(1)
        
    run_committee(args.report_path, args.rounds, args.output, api_key)
