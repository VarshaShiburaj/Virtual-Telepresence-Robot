import socket, traceback
import serial
from time import sleep
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)

p=GPIO.PWM(7,50)
p1=GPIO.PWM(13,50)
p.start(8)
p1.start(7.5)

while 1:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        s.bind(('192.168.1.98', 5555))

        print "Listening for broadcasts..."
        time.sleep(0.2)               
        message, address = s.recvfrom(8192)
        no1,no2,x1,y1,z1,no3,x2,y2,z2=message.split(',')
        print(message)        
        print(z1 ,z2)
        a1=float(z1)
        b1=float(z2)
        s.close();
        
        if(a1>6):      
            a=12.3
            
        elif(a1>5):
            a=11.9
            
        elif(a1>4):
            a=11.2
            
        elif(a1>3):
            a=10.8
        elif(a1>2):
            a=10.5
            
        elif(a1>1):
            a=10.2
            
        elif(a1>0):
            a=9      
            
        elif(a1>-1):
            a=8
            
        elif(a1>-2):
            a=7
            
        elif(a1>-3):
            a=7.5
            
        else:
            a=6.9
        time.sleep(0.2)  

        if(b1>13):
            #b=180#12.5
            b=12.5
        elif(b1>10):
            #b=170#12.3
            b=12.3
        elif(b1>8):
            #b=160#11.7
            b=11.7
        elif(b1>7):
            #b=150#11.1
            b=11.1
        elif(b1>5):
            #b=140#10.5
            b=10.5
        elif(b1>4):
             #b=130#9.9
             b=9.9
        elif(b1>3):
            #b=120#9.3
            b=9.3
        elif(b1>2):
            #b=110#8.7
            b=8.7
        elif(b1>1):
            #b=100#8.1
            b=8.1
        elif(b1>0):
            #b=90 #7.5
            b=7.5  
        elif(b1>-5):
            #b=80#7.3
            b=7.3
        elif(b1>-7):
            #b=60#6.7
            b=6.7
        elif(b1>-9):
            #b=50#6.0
            b=6.0
        elif(b1>-14):
            #b=40#5.3
            b=5.3
        elif(b1>-17):
            #b=30#4.6
            b=4.6
        elif(b1>-20):
            #b=20#3.9
            b=3.9
        elif(b1>-21):
            #b=10#3.2
            b=3.2
        else:
            #b=0#2.5
            b=2.5

        p1.ChangeDutyCycle(b)
        time.sleep(0.4)
        p.ChangeDutyCycle(a)
        time.sleep(0.4)
          
    except (KeyboardInterrupt, SystemExit):
        raise
    except:
        traceback.print_exc()
