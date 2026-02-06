import requests
import json
import sys

def get_stock_info(stock_ids):
    """
    stock_ids: list of strings like ['2330', '6180', '3293']
    自動嘗試上市(tse)和上櫃(otc)兩種市場，根據 API 回傳結果判斷有效股票
    """
    # 為每個代號建立兩種市場的查詢目標
    targets = []
    for sid in stock_ids:
        targets.append(f"tse_{sid}.tw")  # 上市
        targets.append(f"otc_{sid}.tw")  # 上櫃

    url = f"https://mis.twse.com.tw/stock/api/getStockInfo.jsp?ex_ch={'|'.join(targets)}&json=1&delay=0"

    try:
        response = requests.get(url, timeout=10)
        data = response.json()
        if 'msgArray' in data:
            # 過濾掉無效回傳（如無名稱的股票）
            valid_stocks = [s for s in data['msgArray'] if s.get('n') and s.get('n') != '']
            return valid_stocks
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
    return []

if __name__ == "__main__":
    ids = sys.argv[1:] if len(sys.argv) > 1 else ['2330']
    stocks = get_stock_info(ids)
    print(json.dumps(stocks, ensure_ascii=False, indent=2))
