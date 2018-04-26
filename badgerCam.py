import datetime
from picamera import PiCamera 
from time import sleep
from gpiozero import MotionSensor, LED, Button
from signal import pause

def video(time, camera, pir):
    infredLEDs = LED(5)
    infredLEDs.on()
    now = datetime.datetime.now()
    camera.start_recording(now.strftime('%Y-%m-%dT%H:%M:%S') + '.h264')
    camera.wait_recording(time)
    while pir.motion_detected == True:
        print("motion still detected")
        camera.wait_recording(time)
    print("video off")
    camera.stop_recording()
    infredLEDs.off()


def motion_detection_handler(camera, pir):
    print("motion detected")
    video(120, camera, pir)

def check_switch(switch, led):
    if switch.is_pressed == True:
        sleep(1)
        if switch.is_pressed == True:
            print("switch off, exiting")
            led.off()
            exit()

def main():
    print("starting")
    onLED = LED(24)
    onLED.on()
    switch = Button(10)
    check_switch(switch, onLED)
    camera = PiCamera()
    camera.resolution = (1920, 1080)
    pir = MotionSensor(25)
    pir.when_motion = motion_detection_handler(camera, pir)
    while True:
        check_switch(switch, onLED)
        sleep(0.1)


if __name__ == '__main__':
    main()