import requests

url = "https://www.google.com"

r = requests.get(url) #url주소에 데이터 요청

print(r.encoding)

# r.encoding = 'utf-8'
# 응답 객체에 인코딩 지정

# ISO-8859-1
# 각 문자는 단일 8비트 코드 값으로 인코딩.
# 독일어 및 아이슬란드어를 비롯한 여러 언어
# 올바른 인용 부호 제외