from bs4 import BeautifulSoup
import requests

headers = {
  "User-Agent" : "Android"
}

url = "https://www.naver.com"
response = requests.get(url, allow_redirects=True, headers=headers)
response.close()
soup = BeautifulSoup(response.content, "html.parse")
links = []
for a in soup.findAll("a"):
  href = a["href"]
  if href.startswith("#") or href.startswith("@") or href == "/":
    continue
  links.append(href)

data = {
  "url" : url,
  "status_code" : response.status_code,
  "links" : links
}

server_response = requests.post("http://localhost:8080/kisia", json = data)
server_response.close()