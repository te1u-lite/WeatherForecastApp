import requests

# APIキー
API_KEY = "1ed604a220fdd98c96d591c7adb80c80"

# 天気を取得したい都市
city = "神戸市"
lat = 34.69
lon = 135.1955

# APIのエンドポイント
url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric&lang=ja"

response = requests.get(url)
data = response.json()

if response.status_code == 200:
    print(f"{city}の天気: {data['weather'][0]['description']}")
    print(f"気温: {data['main']['temp']}℃")
else:
    print("エラー:", data)
