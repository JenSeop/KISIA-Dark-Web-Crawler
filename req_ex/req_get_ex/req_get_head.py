import requests

url = "https://www.google.com"

r = requests.get(url) #url주소에 데이터 요청

print(r.headers)

# r.headers
# 응답 헤더의 {K:V} 형식의 딕셔너리 자료반환