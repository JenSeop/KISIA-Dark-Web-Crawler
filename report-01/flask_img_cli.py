from flask import request

img_src = "B:\KISIA-Dark-Web-Crawler\report-01\test.jpg"

files = open(img_src, 'rb')

upload = {'file': files}

res = request.post(' http://127.0.0.1:5000/image/', files = upload)