from machine import Pin, UART
import time

# Khởi tạo UART
uart = UART(0, baudrate=9600, tx=Pin(16), rx=Pin(17))

# Lệnh phát nhạc - phát file số 1
def play_song(song_number):
    command = bytearray([0x7E, 0xFF, 0x06, song_number, 0x00, 0x00, 0xEF])
    uart.write(command)

# Khởi động
while True:
    play_song(2)  # Phát bài hát số 1
    time.sleep(10)  # Chờ 10 giây trước khi phát lại
