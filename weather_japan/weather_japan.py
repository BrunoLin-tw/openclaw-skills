# weather_japan.py
# OpenClaw skill: 查詢日本各地天氣預報（今日～明後天）
# 依賴: requests, xml.etree.ElementTree (Python 標準庫)

import sys
import json
import requests
import xml.etree.ElementTree as ET
from typing import Dict, List, Optional

# 全域快取（單次執行不會重複下載，但 OpenClaw 每次呼叫是新 process，所以仍需載入）
CITY_MAP: Dict[str, Dict] = {}

def load_city_codes() -> None:
    global CITY_MAP
    if CITY_MAP:
        return
    url = "https://weather.tsukumijima.net/primary_area.xml"
    try:
        resp = requests.get(url, timeout=8)
        resp.raise_for_status()
        root = ET.fromstring(resp.content)
        for pref in root.findall(".//pref"):
            pref_name = pref.get("title")
            if not pref_name:
                continue
            for city in pref.findall("city"):
                city_name = city.get("title")
                city_id = city.get("id")
                if city_name and city_id:
                    key = f"{pref_name} {city_name}"
                    CITY_MAP[key] = {"pref": pref_name, "city": city_name, "id": city_id}
    except Exception as e:
        print(f"載入地域資料失敗：{str(e)}", file=sys.stderr)
        sys.exit(1)

def search_city(query: str) -> List[Dict]:
    query = query.strip().lower()
    results = []
    for key, info in CITY_MAP.items():
        if query in key.lower():
            results.append(info)
    return results

def get_weather(city_id: str) -> Optional[dict]:
    url = f"https://weather.tsukumijima.net/api/forecast/city/{city_id}"
    try:
        resp = requests.get(url, timeout=8)
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        print(f"取得天氣失敗（{city_id}）：{str(e)}", file=sys.stderr)
        return None

def format_weather(data: dict) -> str:
    if not data:
        return "無法取得天氣資料。"

    location = data.get("location", {})
    lines = []
    lines.append(f"【{location.get('prefecture', '不明')}　{location.get('city', '不明')} 的天氣】")
    lines.append(f"預報時間：{data.get('publicTimeFormatted', '不明')}")

    for day in data.get("forecasts", [])[:3]:  # 只取前三天
        date_label = day.get("dateLabel", "不明")
        telop = day.get("telop", "不明")
        temp = day.get("temperature", {})
        min_t = temp.get("min", {}).get("celsius")
        max_t = temp.get("max", {}).get("celsius")

        lines.append(f"\n{date_label}（{day.get('date', '不明')}）")
        lines.append(f"天氣：{telop}")
        if max_t is not None or min_t is not None:
            lines.append(f"氣溫：{min_t or '--'}℃ ～ {max_t or '--'}℃")

        rain = day.get("chanceOfRain", {})
        rain_str = [f"{k.replace('T',' ')}: {v}" for k, v in rain.items() if v and v != "0%"]
        if rain_str:
            lines.append("降雨機率：" + " | ".join(rain_str))

    desc = data.get("description", {}).get("text", "").strip()
    if desc:
        lines.append("\n【概況】")
        lines.append(desc[:400] + "..." if len(desc) > 400 else desc)

    return "\n".join(lines)

def main():
    if len(sys.argv) < 2:
        print("用法：weather_japan.py <地名>", file=sys.stderr)
        print("範例：weather_japan.py 札幌", file=sys.stderr)
        sys.exit(1)

    query = " ".join(sys.argv[1:]).strip()
    if not query:
        print("請提供地名", file=sys.stderr)
        sys.exit(1)

    load_city_codes()

    candidates = search_city(query)

    if not candidates:
        print(f"找不到「{query}」相關地點。試試更精確名稱（如「東京」「大阪」「那霸」）。")
        sys.exit(0)

    # 自動選第一個符合（OpenClaw skill 通常期望單一結果）
    if len(candidates) > 1:
        print(f"找到多個結果，選用第一個：{candidates[0]['pref']} {candidates[0]['city']}")

    selected = candidates[0]
    data = get_weather(selected["id"])

    if not data:
        print("天氣查詢失敗，請稍後再試。")
        sys.exit(1)

    result = format_weather(data)
    print(result)

if __name__ == "__main__":
    main()