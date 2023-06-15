import requests

url = "https://www.google.com"

r = requests.get(url) #url주소에 데이터 요청

print(r)

# r.content                 # 응답 데이터(binary형식 내용,이미지파일 등) 
# r.text                    # 응답 데이터(텍스트형식 내용, 텍스트 파일에 씀)
# r.json                    # 응답 데이터 JSON형태
# r.url                     # 해당 url 반환
# r.status_code             # 응답 상태코드 (200 이면 성공)
# r.headers                 # 응답 헤더의 {K:V} 형식의 딕셔너리 자료반환
# r.encoding = 'utf-8'      # 응답 객체에 인코딩 지정