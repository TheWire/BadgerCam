from gpiozero import MotionSensor
from signal import pause

pir = MotionSensor(25)

def on_motion_detected():
    print ("derp")

if __name__ == '__main__':
    pir.when_motion = on_motion_detected
    pause()