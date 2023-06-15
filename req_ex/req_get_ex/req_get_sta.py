import requests

url = "https://www.google.com"

r = requests.get(url) #url주소에 데이터 요청

print(r.status_code)

# r.status_code
# 응답 상태코드 (200 이면 성공)