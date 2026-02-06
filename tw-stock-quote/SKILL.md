---
name: tw-stock-quote
description: Query real-time Taiwan stock market quotes from TWSE (Taiwan Stock Exchange). Use when the user asks for Taiwan stock prices, stock quotes, or real-time market data for specific stock tickers (e.g., 2330, 3293, 2303). Automatically detects whether stocks are listed (上市) or OTC (上櫃) markets.
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
