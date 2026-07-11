import requests
import time

# ==========================
# SBI 日本株スキャナー（サンプル）
# ==========================

# 値上がり率条件（％）
MIN_CHANGE = 3.0

# 売買代金（円）
MIN_VOLUME = 100000000

def scan():
    print("=" * 40)
    print("日本株スキャナー")
    print(time.strftime("%Y-%m-%d %H:%M:%S"))
    print("=" * 40)

    # 実用版ではSBIまたは株価APIから取得します。
    # 今は動作確認用です。

    stocks = [
        {"code": "7011", "name": "三菱重工", "change": 4.2},
        {"code": "8306", "name": "三菱UFJ", "change": 3.5},
        {"code": "7203", "name": "トヨタ", "change": 1.1},
    ]

    print("条件：値上がり率3%以上")
    print()

    for stock in stocks:
        if stock["change"] >= MIN_CHANGE:
            print(
                f"{stock['code']} "
                f"{stock['name']} "
                f"{stock['change']}%"
            )

if __name__ == "__main__":
    scan()
