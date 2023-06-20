import requests
# 데이터를 요청하고자 하는
# url = https://news.naver.com/main/read.nhn?\
# mode=LS2D&mid=shm&sid1=101&sid2=259&oid=009&aid=0004299807
# params를 지정하여 요청하는 것은 url뒤에
# 자동으로 ?와 &연산자로 묶어주는역할

url = "https://news.naver.com/main/read.nhn"

get_params = {
'mode': 'LS2D',
'mid': 'shm',
'sid1': '101',
'sid2': '259',
'oid': '076',
'aid': '0004019827'
}

r = requests.get(url,params=get_params)
print(r.text) 
# 해당 뉴스기사 데이터 가져오는 것 확인
# https://entertain.naver.com/read?oid=076&aid=0004019827