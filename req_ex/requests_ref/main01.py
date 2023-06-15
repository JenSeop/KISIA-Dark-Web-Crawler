import requests

headers1 = {
    "User-Agent" : "Android",
    "Referer" : "https://www.nate.com"
}

# www.naver.com 일전 DNS 발생
# verify = False => 인증서 오류 방지
response = requests.get(
    "http://www.naver.com",
    allow_redirects = False,
    headers = headers1,
    verify=False
    )

headers2 = {
    "User-Agent" : "Windows",
    "Referer" : "https://www.naver.com"
}

if "Location" in response.headers and response.status_code == 302:
    response2 = requests.get(response.headers["Location"],
                             headers = headers2,
                             verify = False,
                             )

fd = open("a.html", "wb")
fd.write(response.content.encode("utf-8"))
fd.close()
print(response.content)