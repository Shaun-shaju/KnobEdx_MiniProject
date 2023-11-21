from time import sleep as sl
import random as rd

def exit_py():    
    print("Do you want to exit Knob Edx")
    cho = input("Enter choice: ")
    if list(cho)[0] in ['y', 'Y']:
        print("Connecting to server...")
        sl(rd.randrange(1,8))
        print("Exiting program... Bye... See you again...")
        sl(rd.randrange(1,8))
        quit()
    elif list(cho)[0] in ['n', 'N']:
        print("Connecting to server...")
        sl(rd.randrange(1,8))
        print("Returning to program...")
    else:
        print("Unknown parameter found...")
        print("Exiting Program...")
        sl(rd.randrange(1,8))
        quit()