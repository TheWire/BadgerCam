import datetime
from picamera import PiCamera 
from gpiozero import MotionSensor, LED, Button
from signal import pause

print("starting")
video_on = False
motion = False
onLED = LED(24)
onLED.on()
switch = Button(10)
switch.when_held = switch_hold_handler
camera = PiCamera()
camera.resolution = (1920, 1080)
pir = MotionSensor(25)
pir.when_motion = motion_detection_handler
pause()

def video(time):
    infredLEDs = LED(5)
    infredLEDs.on()
    now = datetime.datetime.now()
    camera.start_recording(now.strftime('%Y-%m-%dT%H:%M:%S') + '.h264')
    camera.wait_recording(time)
    while motion == True:
        motion = False
        print("motion still detected")
        camera.wait_recording(time)
    print("video off")
    video_on = False
    camera.stop_recording()
    infredLEDs.off()


def motion_detection_handler():
    print("motion detected")
    motion = True
    if video_on == False:
        video_on = True
        video(10)

def switch_hold_handler():
    print("switch off, exiting")
    onLED.off()
    exit()
