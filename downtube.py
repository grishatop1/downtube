import webview
from pytube import YouTube
import threading

from googleapiclient.discovery import build

API_KEY = "AIzaSyDBEeVvXGUd9dAkaDZwm8pvJTdZLG0COgU"

yt = build("youtube", "v3", developerKey=API_KEY)

class VideoProcess:
	def __init__(self, url):
		self.url = url

	def getInfo(self):
		request = yt.videos().list(
			part="snippet",
			id=self.url[-11:]
		)
		response = request.execute()
		snippet = response["items"][0]["snippet"]
		
		title = snippet["title"]
		desc = snippet["description"]
		thumbnail_url = snippet["thumbnails"]["medium"]["url"]

		return [title, desc, thumbnail_url]

	def startDownload(self):
		print("started")
		print(self.url)
		yt = YouTube(self.url, on_progress_callback=self.changeProgress)
		try:
			self.video = yt.streams.first()
		except Exception as e:
			print(e)
		print("hehe")
		try:
			self.video.download()
		except Exception as e:
			print(e)

	def changeProgress(self, stream, chunk, bytes_remaining):
		size = self.video.filesize
		progress = int(((size-bytes_remaining)/size)*100)
		print(progress)

class Api:
	def __init__(self):
		self._window = None
		self.videos = {}

	def set_window(self, window):
		self._window = window

	def newVideo(self, url):
		vid = VideoProcess(url)
		self.videos[url] = vid
		return vid.getInfo()

	def downloadVideo(self, url):
		self.videos[url].startDownload()

	def quit(self):
		self._window.destroy()

if __name__ == "__main__":
	api = Api()
	window = webview.create_window('Downtube', "assets/index.html", frameless=True, js_api=api)
	api.set_window(window)
	webview.start(debug=True)