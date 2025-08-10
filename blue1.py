
'''
from machine import Pin, UART
from time import sleep
import uos

print(uos.uname())
uart = UART(0, 9600)
led = Pin(13, Pin.OUT)
while uart.any():
  data = uart.read()
  print(data)
  sleep(3)
'''
from machine import Pin, UART
import time

# Initialize UART on GP0 (TX) and GP1 (RX)
uart = UART(0, baudrate=9600, tx=Pin(12), rx=Pin(13))

# Function to send data
def send_data(data):
    uart.write(data + '\n')

# Main loop
while True:
    if uart.any():
        received = str(uart.read())
        result = received.split('\\')[0].split('\'')[1]
        print("Received:", result)
    
    # Send a test message
    send_data("Hello from Pico!")
    time.sleep(2)
