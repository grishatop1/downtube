import webview
from pytube import YouTube
import threading

from googleapiclient.discovery import build

API_KEY = "AIzaSyDBEeVvXGUd9dAkaDZwm8pvJTdZLG0COgU"

yt = build("youtube", "v3", developerKey=API_KEY)

def getInfo(url):
	request = yt.videos().list(
		part="snippet",
		id=url[-11:]
	)
	response = request.execute()
	snippet = response["items"][0]["snippet"]
	print(snippet["title"])

class Api:
	def __init__(self):
		self._window = None

	def set_window(self, window):
		self._window = window

	def reqInfo(self, url):
		getInfo(url)
		print("done")

	def quit(self):
		self._window.destroy()

if __name__ == "__main__":
	api = Api()
	window = webview.create_window('Downtube', "assets/index.html", frameless=True, js_api=api)
	api.set_window(window)
	webview.start(debug=True)