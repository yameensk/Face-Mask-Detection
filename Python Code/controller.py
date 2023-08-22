from pyfirmata import Arduino,SERVO
import time

port = 'COM5'
pin = 5

board=Arduino(port)
board.digital[pin].mode = SERVO

def rotateServo(pin, angle): 
    board.digital[pin].write(angle) 

def doorAutomate(val):
    if val==1: 
        rotateServo(pin,110)        # Door Open position
        board.digital[3].write(0)   # Green Led ON
        board.digital[4].write(1)   # Red Led OFF

    elif val==0:
        rotateServo(pin, 10)        # Door Close position
        board.digital[3].write(1)   # Red Led ON
        board.digital[4].write(0)   # Green Led OFF