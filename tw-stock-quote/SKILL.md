---
name: tw-stock-quote
description: Query real-time Taiwan stock market quotes from TWSE (Taiwan Stock Exchange). Use when the user asks for Taiwan stock prices, stock quotes, or real-time market data for specific stock tickers (e.g., 2330, 3293, 2303). Automatically detects whether stocks are listed (上市) or OTC (上櫃) markets.
author: Bruno Lin
author-email: lin.bruno@gmail.com
version: 1.0.0
metadata: {"openclaw":{"emoji":"📈","requires":{"bins":["python3"],"env":[]}}}
---

# Taiwan Stock Quote

查詢台灣股市即時報價（上市/上櫃自動判斷）

## Quick Start

查詢單一或多檔股票即時報價：

```bash
python3 scripts/get_tw_stock.py <股票代號1> <股票代號2> ...
```

**範例：**
```bash
python3 scripts/get_tw_stock.py 2330 3293 2303
```

## How It Works

1. **自動市場判斷**：腳本同時向 TWSE API 查詢上市（tse）和上櫃（otc）兩個市場
2. **過濾無效資料**：API 只回傳有效的股票資料
3. **完整報價資訊**：包含成交價、漲跌、開高低、成交量、最佳五檔等

## Response Fields

| 欄位 | 說明 |
|------|------|
| `z` | 最新成交價 |
| `y` | 昨日收盤價 |
| `o` | 今日開盤價 |
| `h` | 今日最高價 |
| `l` | 今日最低價 |
| `v` | 成交量（張） |
| `n` | 股票簡稱 |
| `nf` | 公司全名 |
| `ex` | 市場別（tse=上市, otc=上櫃） |
| `a` / `b` | 最佳五檔 賣價 / 買價 |

## Resources

### scripts/
- `get_tw_stock.py` - 主要查詢腳本

## Metadata

依照 <https://docs.openclaw.ai/tools/skills#format-agentskills-+-pi-compatible>，`SKILL.md` 需要在 front-matter 定義一個單行 `metadata` JSON，`metadata.openclaw` 可以宣告 `emoji`、`requires`（例如 `bins`、`env`、`config`）、`primaryEnv` 等欄位，幫助 OpenClaw 判斷該 skill 的可用性與顯示資訊。上方範例同時提供 emoji 與要求的 `python3` 執行環境。

## Copyright

本文件與相關腳本由 Bruno Lin (lin.bruno@gmail.com) 編寫，並依據MIT 授權進行發佈，使用、複製或修改前請先詳閱該授權條款。
