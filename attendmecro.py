import pyautogui
import keyboard
import time

pyautogui.FAILSAFE = True  # 마우스를 화면 좌상단에 두면 긴급 종료

print("5초 안에 입력창을 클릭하세요! (ESC 키로 종료 가능)")
time.sleep(5)

for i in range(100, 1000):
    if keyboard.is_pressed('esc'):
        print("ESC 키가 눌려 매크로를 중단합니다.")
        break
    
    num = f"{i:03}"
    pyautogui.write(num, interval=0.05)
    pyautogui.press('enter', interval=0.05)
    pyautogui.press('enter', interval=0.05)
    pyautogui.click()
    pyautogui.press('backspace', interval=0.05)
    pyautogui.press('backspace', interval=0.05)
    pyautogui.press('backspace', interval=0.05)

    time.sleep(0.3)
