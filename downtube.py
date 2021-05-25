import webview
import pytube

webview.create_window('Downtube', "assets/index.html", frameless=True)
webview.start(debug=True)