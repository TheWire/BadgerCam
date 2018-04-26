import datetime
from picamera import PiCamera 
from time import sleep
from gpiozero import MotionSensor, LEd, Button
from signal import pause

def video(int time, PiCamera camera, MotionSensor pir):
    infredLEDs = LED(17)
    infredLEDs.on()
    now = datetime.datetime.now()
    camera.start_recording(now.strtime('%Y-%m-%dT%H:%M:%S') + '.h264')
    while pir.is_pressed == True:
        camera.wait_recording(time)
    camera.stop_recording()
    infredLEDs.off()


def motion_detection_handler(PiCamera camera, MotionSensor pir):
    video(120, camera, pir)

def check_switch():
    if switch.is_pressed == True:
        sleep(1)
        if switch.is_pressed == True:
            exit()

def main():
    camera = PiCamera()
    switch = Button(2)
    pir = MotionSensor(25)
    pir.when_motion = motion_detection_handler(camera, pir)
    while True:
        check_switch(switch)
        sleep(0.1)


if __name__ == '__main__':
    main()