import requests

url = "https://www.google.com"

r = requests.get(url) #url주소에 데이터 요청

print(r.url)

# r.url
# 해당 url 반환