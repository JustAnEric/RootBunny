from rootbunny.extensions.Extension import BaseExtension
from flask import send_file
# DO NOT REMOVE OR EDIT!
# This file handles all DOM events and manipulation.
# It is important to keep this file so that API bindings are created on the client.

class Extension(BaseExtension):
    def __init__(self, window):
        super().__init__(window)
        self.appid = "RootBunny"
        
        self.window.register_app("RootBunny", "1.2.1", "RootBunny")
        self.request_server_bindings([
            '/default/wallpaper'
        ])
        
    def proxy_route(self, route:str):
        if route == "default/wallpaper":
            return send_file('./content/extensions/ROOT/wallpaper.jpg')
        
    def start(self):
        print("Started core RootBunny extension")