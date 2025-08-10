from machine import Pin, UART
import time

# Cấu hình UART
uart = UART(0, baudrate=9600, tx=Pin(16), rx=Pin(17))

def send_command(command):
    # Gửi lệnh đến DFPlayer Mini
    uart.write(command)

def play_all_tracks():
    # Phát tất cả các bài hát trong thẻ SD
    for track_number in range(1, 10):  # Giả định có tối đa 254 bài hát
        send_command(bytes([0x7E, 0xFF, 0x06, 0x03, track_number, 0x00, 0x00, 0x7E]))  # Lệnh phát bài
        time.sleep(5)  # Chờ 5 giây trước khi phát bài tiếp theo
        # Dừng phát sau khi phát bài, nếu cần
        send_command(b'\x7E\xFF\x06\x16\x00\x00\x00\x7E')  # Lệnh dừng phát
        time.sleep(1)  # Chờ 1 giây trước khi phát bài tiếp theo

# Gọi hàm phát tất cả bài hát
play_all_tracks()