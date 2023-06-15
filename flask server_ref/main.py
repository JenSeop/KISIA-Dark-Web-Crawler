### flask 모듈의 Flask 웹 프레임워크와,
### 클라이언트 요청에 대한 객체 request
### 미리 임포트
from flask import Flask, request
# 플라스크 객체 선언
app = Flask(__name__)

# 디렉토리 경로 설정과 허용하고자 하는 메서드를 정의
@app.route("/kisia", methods=["GET", "POST"])
# 실제 동작하는 함수
def kisia():
    # 클라이언트의 요청 객체
    params = json.loads(request.get_data())
    print(params["1"])
    # 리턴값은 200 OK
    return "kisia", 200

if __name__ == "__main__":
    # app.run 통해 웹 구동
    # debug 디버깅 메시지 출력
    # host = 0.0.0.0 / 모든 IP 대역 받아들임
    # port = 서비스 하고자 하는 tcp 80000
    app.run(debug=True, host='0.0.0.0', port=8080)