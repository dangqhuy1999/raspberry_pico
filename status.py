from machine import Pin, UART
import time

# Thiết lập cổng UART
uart = UART(1, baudrate=9600, tx=8, rx=9)  # TX ở GPIO 0, RX ở GPIO 1

def send_command(command):
    uart.write(command)
    time.sleep(0.1)

def play_track(track_number):
    command = bytes([0x7E, 0xFF, 0x06, track_number, 0x00, 0x00, 0xEF])
    send_command(command)

def stop_playback():
    command = bytes([0x7E, 0xFF, 0x16, 0x00, 0x00, 0x00, 0xEF])
    send_command(command)

def check_status():
    command = bytes([0x7E, 0xFF, 0x3A, 0x00, 0x00, 0x00, 0xEF])
    send_command(command)
    time.sleep(0.5)
    if uart.any():  # Kiểm tra dữ liệu phản hồi
        response = uart.read(10)  # Đọc phản hồi (10 byte)
        print("Response:", response)

def get_current_track():
    command = bytes([0x7E, 0xFF, 0x3F, 0x00, 0x00, 0x00, 0xEF])
    send_command(command)
    time.sleep(0.5)
    if uart.any():
        response = uart.read(10)  # Đọc phản hồi (10 byte)
        print("Current Track Response:", response)
def set_volume(volume):
    # Đảm bảo âm lượng nằm trong khoảng từ 0 đến 30
    if 0 <= volume <= 30:
        command = bytes([0x7E, 0xFF, 0x06, volume, 0x00, 0x00, 0xEF])
        send_command(command)
    else:
        print("Volume must be between 0 and 30.")
# Ví dụ sử dụng
try:
    set_volume(10)
    for i in range (1,254):
        
        play_track(254)  # Chạy track 1
        time.sleep(2)  # Chờ 10 giây
        stop_playback()  # Dừng phát
    check_status()  # Kiểm tra trạng thái
    get_current_track()  # Lấy số track hiện tại
except Exception as e:  # Sửa lỗi ở đây
    print("An error occurred:", e)