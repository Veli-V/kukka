import serial
import pyttsx3
import time

print(time.strftime("%H:%M", time.localtime()))

ser = serial.Serial('/dev/cu.usbmodem144101')

engine = pyttsx3.init()
#engine.say('Good morning.')
#engine.runAndWait()

#ser.write("aaa".encode())

timeStr = time.strftime("%H:%M", time.localtime())
morningLine = "Good Morning! It's time to lift your lazy ass from to bed. Time is: " + timeStr + " This means you're already late! But now, news from the flower!"
print(morningLine)
# READ data from arduino and read it
ser_bytes = ser.readline()
line = ser_bytes.decode('utf-8')
print(line)
#engine.say(morningLine)
engine.say(line)
engine.runAndWait()
