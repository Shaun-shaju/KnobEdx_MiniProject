from time import sleep as sl
import random as rd
import webview

def start(sentence):        
    webview.create_window('Watch Video -- KnobEdx', f'https://www.google.com/search?q={sentence}')
    webview.start()

def textbook(classs, sylab):
    chapter = input("Enter your chapter: ")
    gud = input("Do you want a guide (yes or no): ")
    if list(gud)[0] in ['y', 'Y']:
        print("Your textbook is being fetched... Check your taskbar for new windows...")
        print("Connecting to server...")  
        sl(rd.randrange(1,8))              
        sen = f'class {classs} {sylab} guide pdf for chapter {chapter}'   
        start(sen) 
    elif list(gud)[0] in ['n', 'N']:    
        print("Your textbook is being fetched... Check your taskbar for new windows...")
        print("Connecting to server...")  
        sl(rd.randrange(1,8))              
        sen = f'class {classs} {sylab} textbook pdf for chapter {chapter}'   
        start(sen) 
    else:
        print("Unknown parameter found...")
        print("Exiting Program...")
        sl(rd.randrange(1,8))