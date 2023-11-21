import urllib.request
import re
import webview
from time import sleep as sl
import random as rd

def video():
	query = input("Enter your question: ")
	print("Your video is starting... Check the taskbar for a new window...")
	print("Connecting to server...")
	sl(rd.randrange(2,5))
	que_str = query.split(" ")
	senc = ''
	for a in que_str:
		senc += a
	html = urllib.request.urlopen(f"https://www.youtube.com/results?search_query={senc}")
	video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
	webview.create_window('Watch Video -- KnobEdx', f'https://www.youtube.com/watch?v={video_ids[0]}')
	webview.start()