import os
import requests
from dotenv import load_dotenv

load_dotenv()

# APIキー
API_KEY = os.getenv("OPENWEATHER_API_KEY")

if not API_KEY:
    raise ValueError("環境変数 'API_KEY' が設定されていません。")

# 天気を取得したい都市
city = "神戸市"
lat = 34.69
lon = 135.1955

# APIのエンドポイント
url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric&lang=ja"

# APIリクエスト
response = requests.get(url)
data = response.json()

if response.status_code == 200:
    # 現在の天気
    current_weather = data["weather"][0]["description"]
    current_temp = data["main"]["temp"]

    # 今日の気温
#     print(f"現在の{city}の天気: {current_weather}")
#     print(f"現在の気温: {current_temp}℃")
# else:
#     print("エラー:", data)


#SlackAPI
TOKEN = os.getenv("SLACK_TOKEN")
CHANNEL = os.getenv("SLACK_CHANNEL")

url = "https://slack.com/api/chat.postMessage"
headers = {"Authorization": "Bearer "+TOKEN}
data = {
    "channel": CHANNEL,
    "text": f"現在の{city}の天気: {current_weather}"+"\n"+f"現在の気温: {current_temp}℃"
}
r =requests.post(url,headers=headers,data=data)
#print("return",r.json())