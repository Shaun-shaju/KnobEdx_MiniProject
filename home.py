from video import video
from test import test
from doubt_clear import doubt
from textbook import textbook
from exit import exit_py
from time import sleep as sl
import random as rd

def home():
    name = ''
    classs = ''
    sylb = ''
    with open("./tmp_knobedx/log.knobedx", '+r') as k:
        lines = k.read().splitlines()
        user = lines[-1]
    with open("./tmp_knobedx/student.knobedx", '+r') as k:
        lines = k.read().splitlines()
        for a in lines:
            lt = eval(a)
            if user == lt[0]:
                name += str(lt[1])
                classs += str(lt[2])                
                sylb += str(lt[5])
            else:
                pass
    while True:
        print(" ")
        print(f"Hi, {name}")
        print(" ")
        print('''------------------- Menu
              
            1) Watch Video
            2) Read Textbook
            3) Take Test / Assesments
            4) Clear Doubt
            5) Exit Program # Print Log''')
        print(" ")
        choice = int(input("Enter choice index no.: "))
        if choice == 1:
            video()
            print(" ")
            print("Connecting to server...")
            sl(rd.randrange(1,8))
        elif choice == 2:
            textbook(classs, sylb)
            print(" ")
            print("Connecting to server...")
            sl(rd.randrange(1,8))
        elif choice == 3:
            sub = input("Enter subject: ")
            query = input("Enter your test topic: ")
            test(classs, sylb, query, sub)
            print(" ")
            print("Connecting to server...")
            sl(rd.randrange(1,8))
        elif choice == 4:            
            sub = input("Enter subject name your query comes under: ")
            chapt = input("Enter the chapter name of your query: ")
            doubt(classs, sylb, chapt, sub)
            print(" ")
            print("Connecting to server...")
            sl(rd.randrange(1,8))
        elif choice == 5:
            exit_py()
            print("Connecting to server...")
            sl(rd.randrange(1,8))
        else:
            print("Unknown parameter found...")
            print("Exiting Program...")
            sl(rd.randrange(1,8))
            quit()