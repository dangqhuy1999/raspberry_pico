from dfplayermini import DFPlayerMini
import time

player1 = DFPlayerMini(0, 16, 17)



print ("Set SD Card")
read_value = player1.select_source('sdcard')

print ("Read volume")
read_value = player1.get_volume()
print (f"Volume {read_value}")

print ("Set Volume 12")
read_value = player1.set_volume(12)

print ("Read volume")
read_value = player1.get_volume()
print (f"Volume {read_value}")


print ("Read Num files")
read_value = player1.query_num_files()
print (f"Num files {read_value}")

print ("Play 01")
read_value = player1.play(1)

time.sleep(10)

print ("Play 02")
read_value = player1.play(2)

time.sleep(10)

print ("Play Next")
read_value = player1.play_next()

time.sleep(5)

print ("Pause")
read_value = player1.pause()

time.sleep(2)

print ("Resume")
read_value = player1.start()

time.sleep(5)

print ("Stop")
read_value = player1.stop()