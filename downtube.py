import webview
from pytube import YouTube
import socket

from googleapiclient.discovery import build

API_KEY = "AIzaSyDBEeVvXGUd9dAkaDZwm8pvJTdZLG0COgU"
yt = build("youtube", "v3", developerKey=API_KEY)
socket.setdefaulttimeout(5)

class VideoProcess:
	def __init__(self, url):
		self.url = url
		self.netError = False

	def getInfo(self):
		request = yt.videos().list(
			part="snippet",
			id=self.url[-11:]
		)
		try:
			response = request.execute()
		except:
			api._window.evaluate_js("setVideoNotFound()")
			self.netError = True
			return
		if not response["items"]:
			api._window.evaluate_js("setVideoNotFound()")
			self.netError = True
			return
		snippet = response["items"][0]["snippet"]
		
		self.title = snippet["title"]
		self.desc = snippet["description"]
		self.thumbnail_url = snippet["thumbnails"]["medium"]["url"]

		self.netError = False
		return [self.title, self.desc, self.thumbnail_url]

	def startDownload(self):
		yt = YouTube(self.url, 
		on_progress_callback=self.changeProgress,
		on_complete_callback=self.complete)
		if self.netError:
			api._window.evaluate_js("reset()")
		try:
			api._window.evaluate_js("setProgressText('GETTING INFO...')")
			self.video = yt.streams.first()
		except Exception as e:
			print(e)
		try:
			api._window.evaluate_js("setProgressText('STARTING DOWNLOAD...')")
			self.video.download("Downloads/Video/")
		except Exception as e:
			print(e)
	
	def startDownloadAudio(self):
		yt = YouTube(self.url, 
		on_progress_callback=self.changeProgress,
		on_complete_callback=self.complete)

		if self.netError:
			api._window.evaluate_js("reset()")

		try:
			api._window.evaluate_js("setProgressText('GETTING INFO...')")
			self.video = yt.streams.filter(only_audio=True).first()
		except Exception as e:
			print(e)
			print("filter exp")

		try:
			api._window.evaluate_js("setProgressText('STARTING DOWNLOAD...')")
			self.video.download("Downloads/Audio/")
		except Exception as e:
			print(e)
			print("down exp")

	def changeProgress(self, stream, chunk, bytes_remaining):
		size = self.video.filesize
		progress = int(((size-bytes_remaining)/size)*100)
		api._window.evaluate_js("setProgressBarWidth("+str(progress)+")")
		api._window.evaluate_js("setProgressText('DOWNLOADING...')")
		api._window.evaluate_js("setPercentText("+str(progress)+")")

	def complete(self, stream, fp):
		api._window.evaluate_js("setDownloaded()")

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

	def downloadAudio(self, url):
		self.videos[url].startDownloadAudio()

	def quit(self):
		self._window.destroy()

if __name__ == "__main__":
	api = Api()
	window = webview.create_window('Downtube', "assets/index.html", frameless=True, js_api=api)
	api.set_window(window)
	webview.start(debug=True)