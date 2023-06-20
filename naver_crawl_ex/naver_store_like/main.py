import requests

headers={
    "Host":"search.shopping.naver.com",
    "Content-Type":"application/json",
    "Cookie":"",
    "Referer":"https://search.shopping.naver.com/search/all?where=all&frm=NVSCTAB&query=%EC%82%BC%EA%B2%B9%EC%82%B4",
    "Sbth":"0e067b473eba76cf1fc405a4baaf65939b1b8e4b0b2abd09c0c0349a55cd46292ef71dc78b8d3f43eeacfab441fad2ec",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

url="https://search.shopping.naver.com/api/product-zzim/add"
data={
    "chpid": "",
    "isAd": "",
    "isAdult":"",
    "isBook": "",
    "isHotdeal": "",
    "nvMid":"",
    "tr":""
}
response=requests.post(url,headers=headers,json=data,verify=False)
print(response.content)