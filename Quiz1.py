
import RPi.GPIO as GPIO
import time

GREEN = 17
RED = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(GREEN, GPIO.OUT)
GPIO.setup(RED, GPIO.OUT)
GPIO.setwarnings(False)
score = 0
print ("===== Python Quiz Game =====")

# Q1
ans1 = input("1. Which is not a Python data type?\na) int\nb) float\nc) rational\nd) str\nAnswer: ")
if ans1.lower() == "c":  
    print ("Correct!")
    GPIO.output(GREEN, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(GREEN, GPIO.LOW)
    score +=1
else:
    print ("Wrong!")
    GPIO.output(RED, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(RED, GPIO.LOW)
# Q2
ans2 = input("2. Which is not a built-in function?\na) print()\nb) input()\nc) len()\nd) sqrt()\nAnswer: ")
if ans2.lower() == "d":
    print ("Correct!")
    GPIO.output(GREEN, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(GREEN, GPIO.LOW)
    score +=1
else:
    print ("Wrong!")
    GPIO.output(RED, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(RED, GPIO.LOW)
# Q3
ans3 = input("3. If you mix int and float, what happens?\na) Error\nb) Float becomes int\nc) Int becomes float\nd) No change\nAnswer: ")
if ans3.lower() == "c":
    print ("Correct!")
    GPIO.output(GREEN, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(GREEN, GPIO.LOW)
    score +=1
else:
    print ("Wrong!")
    GPIO.output(RED, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(RED, GPIO.LOW)
# Q4
ans4 = input("4. Which is for multiple choices?\na) if\nb) if-else\nc) if-elif-else\nd) loop\nAnswer: ")
if ans4.lower() == "c":
    print ("Correct!")
    GPIO.output(GREEN, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(GREEN, GPIO.LOW)
    score +=1
else:
    print ("Wrong!")
    GPIO.output(RED, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(RED, GPIO.LOW)
# Q5
ans5 = input("5. Which keyword stops a loop?\na) continue\nb) break\nc) stop\nd) exit\nAnswer: ")
if ans5.lower() == "b":
    print("Correct!")
    GPIO.output(GREEN, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(GREEN, GPIO.LOW)
    score +=1
else:
    print("Wrong!")
    GPIO.output(RED, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(RED, GPIO.LOW)
print (f"\nFinal Score: {score}/5")
GPIO.cleanup()
