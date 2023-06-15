import requests

url = "https://www.google.com"

r = requests.get(url) #url주소에 데이터 요청

print(r.text)

# r.text
# 응답 데이터(텍스트형식 내용, 텍스트 파일에 씀)