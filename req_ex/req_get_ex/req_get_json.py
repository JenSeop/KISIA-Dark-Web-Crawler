import requests

url = "https://www.google.com"

r = requests.get(url) #url주소에 데이터 요청

print(r.json)

# r.json
# 응답 데이터 JSON형태