import machine
import utime

led_onboard = machine.Pin(25, machine.Pin.OUT)
#huydang
while True:
  led_onboard.value(1)
  utime.sleep_ms(1000)
  led_onboard.value(0)
  utime.sleep_ms(1000)
