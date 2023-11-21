import urllib.request
import re
import webview
from time import sleep as sl
import random as rd
from bs4 import BeautifulSoup
import requests

def ext(url):
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
    html = requests.get(url,headers=headers)
    soup = BeautifulSoup(html.text, 'html.parser')
    allData = soup.find_all("div",{"class":"g"})
    g=0
    Data = [ ]
    l={}
    for i in range(0,len(allData)):
        link = allData[i].find('a').get('href')
        if(link is not None):
            if(link.find('https') != -1 and link.find('http') == 0 and link.find('aclk') == -1):
                g=g+1
                l["link"]=link
                Data.append(l)
                l={}
            else:
                continue
        else:
            continue
    linkw = Data[0]['link']    
    webview.create_window('Take Test -- KnobEdx', linkw)
    webview.start()     

def test(classs, sylab, query, subject):
	print("Your test is starting... Check the taskbar for a new window...")
	print("Connecting to server...")
	sl(rd.randrange(2,5))
	sen = f'class {classs} {sylab} mcq for {subject} chapter {query} from physics gurukul'
	ext(f"https://www.google.com/search?q={sen}")