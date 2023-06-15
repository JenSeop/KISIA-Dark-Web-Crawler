import requests

url = "https://www.google.com"

r = requests.get(url) #url주소에 데이터 요청

print(r.content)

# r.content
# 응답 데이터(binary형식 내용,이미지파일 등)