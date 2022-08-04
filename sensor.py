import time
import RPi.GPIO as GPIO


class Sensor:
    def __init__(self, trig, echo):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)

        self.trig = trig
        self.echo = echo

        self.setup()

    def setup(self):
        GPIO.setup(self.trig, GPIO.OUT)
        GPIO.setup(self.echo, GPIO.IN)
        GPIO.output(self.trig, GPIO.LOW)
        time.sleep(1)

    def clean(self):
        GPIO.cleanup()

    def read(self):
        GPIO.output(self.trig, True)
        time.sleep(0.00001)
        GPIO.output(self.trig, False)
 
        while GPIO.input(self.echo) == 0:
          signaloff = time.time()
         
        while GPIO.input(self.echo) == 1:
          signalon = time.time()
 
        timepassed = signalon - signaloff
        distance = timepassed * 17000
        return distance
         
if __name__ == "__main__":
    sensor = Sensor(11, 13)
    for i in range(400):
        print(sensor.read())
    sensor.clean()
