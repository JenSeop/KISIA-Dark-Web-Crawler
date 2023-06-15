import requests

headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win32; x86) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36"
}

response = requests.get(
    "http://www.nate.com",
    allow_redirects = False,
    headers = headers,
    verify=False
    )


if "Location" in response.headers and response.status_code == 302:
    response2 = requests.get(response.headers["Location"],
                             headers = headers,
                             verify = False,
                             )

fd = open("a.html", "wb")
fd.write(response.content)
fd.close()
print(response.content)