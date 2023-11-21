from time import sleep as sl
import random as rd
import stdiomask as st

def signup():
    print(" ")
    print("---------- Signup - Knob Edx ----------")
    sl(rd.randrange(2,5))
    print("Connecting to server...")
    sl(rd.randrange(1,3))
    name = input("Enter student name: ")
    class_st = input("Enter Class: ")
    school = input("Enter School Name: ")
    phone = input("Enter parent's phonenumber: ")
    user = input("Enter username: ")
    sylb = input("Enter syllabus (ncert, icse, etc no caps): ")
    passcode = st.getpass(prompt='Enter passcode: ')
    print(" ")
    print(f"Welcome to Knob Edx {user} ...")
    with open("./tmp_knobedx/user.knobedx", '+a') as f:
        f.writelines(f"{user} | {passcode}\n")
    with open("./tmp_knobedx/student.knobedx", '+a') as f:
        f.writelines(f"['{user}', '{name}', '{class_st}', '{school}', '{phone}', '{sylb}'] \n")
    print("Restarting Program...")
    sl(rd.randrange(1,8))
    quit()