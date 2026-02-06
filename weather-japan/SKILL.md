---
name: weather-japan
description: 查詢日本各地今日、明日、明後天的天氣預報（來自日本氣象廳資料，tsukumijima.net API）
author: Bruno Lin (Modified by Bruno Lin)
author-email: lin.bruno@gmail.com
version: 1.0.0
metadata: {"openclaw":{"emoji":"⛅","requires":{"bins":["python3"],"env":[]}}}
---

# 日本天氣查詢 skill

這個 skill 可以讓你快速查詢日本任何城市/地區的短期天氣預報（今日～明後天）。

## 使用方式

直接告訴 agent：

- 「札幌今天天氣如何？」
- 「東京明天會下雨嗎？」
- 「查一下大阪後天的氣溫」
- 「那霸現在的天氣預報」

支援模糊搜尋，大多數城市名稱都可以（例如「京都」「仙台」「福岡」「沖繩」等）。

### 命令列使用範例

如果要直接呼叫腳本，可以執行：

```bash
python3 weather_japan.py 札幌
```

上述指令會先載入日本地點對應表，搜尋包含「札幌」的 city id，並回傳格式化後的今日～明後天天氣描述（含氣溫與降雨機率）。

## 內部執行邏輯

1. 從 https://weather.tsukumijima.net/primary_area.xml 載入約 2000 個日本地點對應表
2. 根據輸入地名進行部分匹配搜尋
3. 若有多個候選，自動選用第一個最符合的
4. 呼叫 https://weather.tsukumijima.net/api/forecast/city/{id} 取得 JSON
5. 格式化輸出今日/明日/明後天的天氣、氣溫、降雨機率與概況文字

## 依賴

- Python 3（內建 requests 與 xml 模組）
- 網路連線（用來下載地域表與天氣 JSON）

## 範例輸出樣式

【東京都　東京 的天氣】
預報時間：2026/02/05 11:00

今日（2026-02-05）
天氣：晴時多雲
氣溫：8℃ ～ 14℃
降雨機率：06-12: 10% | 12-18: 20%

明日（2026-02-06）
...

【概況】
關東地方は高気圧に覆われて...

## 注意事項

- 資料來源為日本氣象廳 → 非官方包裝 API，準確度高但偶有延遲
- 冬季北海道等地常有「雪」或「暴風雪」預報，請注意低溫
- 若找不到地點，可試加上都道府縣名稱（如「北海道 札幌」）

享受日本天氣查詢吧！⛅

## Copyright

本文件與相關腳本由 Bruno Lin (lin.bruno@gmail.com) 編寫，並依據MIT 授權進行發佈，使用、複製或修改前請先詳閱該授權條款。
