from time import sleep as sl
import random as rd
import stdiomask as st
from signup import signup


with open("./tmp_knobedx/user.knobedx") as f:
    lines = f.readlines()

if lines == []:
    print(" ")
    print("No users found in your database... Do you want to sign up?")
    cho = input("Enter choice: ")
    if list(cho)[0] in ['y', 'Y']:
        print("Connecting to server...")
        signup()
    elif list(cho)[0] in ['n', 'N']:
        print("Connecting to server...")
        print("Exiting Program...")
        sl(rd.randrange(1,8))
        quit()
    else:
        print("Unknown parameter found...")
        print("Exiting Program...")
        sl(rd.randrange(1,8))
        quit()

else:
    users = {}
    for a in lines:
        lt = a.split(' | ')
        pa = lt[1].split('\n')
        passcode = pa[0]
        for b in lt:
            users[lt[0]] = str(passcode)

    def login():
        print(" ")
        print("---------- Login - Knob Edx ----------")
        print("Connecting to server...")
        sl(rd.randrange(1,3))
        user = input("Enter username: ")
        passcode = st.getpass(prompt='Enter passcode: ')
        if user in users:
            if users[user] == passcode:
                print("Access Granted")
                with open("./tmp_knobedx/log.knobedx", '+a') as k:
                    k.writelines(f"{user}\n")
            else:
                print(f"Access Denied for user: '{user}' because of wrong password.")
        else:
            print("User not found... Do you want to sign up?")
            cho = input("Enter choice: ")
            if list(cho)[0] in ['y', 'Y']:
                print("Connecting to server...")
                signup()
            elif list(cho)[0] in ['n', 'N']:
                print("Connecting to server...")
                print("Exiting Program...")
                sl(rd.randrange(1,8))
                quit()
            else:
                print("Unknown parameter found...")
                print("Exiting Program...")
                sl(rd.randrange(1,8))
                quit()