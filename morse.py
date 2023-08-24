import os
import time

# 사용할 GPIO 번호
gpio_89 = 89

# GPIO 초기 설정
os.system(f"echo {gpio_89} > /sys/class/gpio/export")
os.system(f"echo out > /sys/class/gpio/gpio{gpio_89}/direction")

# 모스 부호에 사용할 문자와 부호를 정의합니다.
morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', ' ': '/'
}

# 단위 시간 (초)
dot_duration = 0.3

def led_on():
    os.system(f"echo 1 > /sys/class/gpio/gpio{gpio_89}/value")

def led_off():
    os.system(f"echo 0 > /sys/class/gpio/gpio{gpio_89}/value")

def morse_blink(symbol):
    for char in symbol:
        if char == '.':
            led_on()
            time.sleep(dot_duration)
            led_off()
        elif char == '-':
            led_on()
            time.sleep(dot_duration * 3)
            led_off()
        # 간과 간 사이는 1초로 설정
        time.sleep(dot_duration)

def main():
    while True:
        text = input("모스 부호로 변환할 문자열을 입력하세요 (영문 대문자와 숫자만 가능): ")
        for char in text:
            if char.upper() in morse_code:
                symbol = morse_code[char.upper()]
                morse_blink(symbol)
            else:
                print(f"'{char}'는 모스 부호로 변환할 수 없는 문자입니다.")
        print("전송 완료")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        os.system(f"echo {gpio_89} > /sys/class/gpio/unexport")