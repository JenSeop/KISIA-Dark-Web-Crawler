import requests

# 요청시 헤더정보를 크롬으로 지정
request_headers = { 
'User-Agent' : ('Mozilla/5.0 (Windows NT 10.0;Win64; x64)\
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98\
Safari/537.36'), } 

url = "https://search.naver.com/search.naver"
response = requests.get(url,headers = request_headers)

print(response) 
#해당 url 요청할 때 headers를 임의로 설정하여 요청한 케이스