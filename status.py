from machine import Pin, UART
import utime

# Thiết lập cổng UART
uart = UART(0, baudrate=9600, tx=16, rx=17)  # TX ở GPIO 0, RX ở GPIO 1

def send_command(command):
    uart.write(command)
    utime.sleep(0.1)
    if uart.any():
        response = uart.read()
        print("Response:", response)
    else:
        print("No response from DFPlayer.")
def play_track(track_number):
    command = bytes([0x7E, 0xFF, 0x06, 0x03, 0x01, track_number, 0x00, 0xEF])
    send_command(command)

try:
    
    for i in range (1,4):
        play_track(i)  # Chạy track 1
        utime.sleep(225)  # Chờ 10 giây
except Exception as e:  # Sửa lỗi ở đây
    print("An error occurred:", e)