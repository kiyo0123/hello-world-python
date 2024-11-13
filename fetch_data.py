import requests

# API URLを変数にする
url = "https://jsonplaceholder.typicode.com/users/3"

try:
    # APIからデータを取得
    response = requests.get(url)
    response.raise_for_status()  # ステータスコードが200でない場合に例外を発生させる

    # JSONデータを解析して出力
    data = response.json()
    print("User data fetched successfully!")
    print("Name:", data["name"])
    print("Email:", data["email"])

except requests.exceptions.RequestException as e:
    # エラー内容を出力
    print("Failed to fetch data:", e)

