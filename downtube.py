import webview
import pytube


class Api:
	def __init__(self):
		self._window = None

	def set_window(self, window):
		self._window = window

	def quit(self):
		self._window.destroy()

if __name__ == "__main__":
	api = Api()
	window = webview.create_window('Downtube', "assets/index.html", frameless=True, js_api=api)
	api.set_window(window)
	webview.start(debug=True)