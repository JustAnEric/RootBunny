from rootbunny.extensions.Extension import BaseExtension

class Extension(BaseExtension):
    def __init__(self, window):
        super().__init__(window)
        
        self.appid = "Spotify"
        
        #@self.event(self.BaseExtensionEvent.ONLOAD_EVENT)
        #def route():
            #self.window.load('https://open.spotify.com')
        #print(self.window.window.get_cookies())
        
        self.window.register_app("Spotify", 1, self.appid, self.onOpen, self.onClose)
        self.request_server_bindings([
            '/apps/spotify'
        ])
        
    def onOpen(self):
        print("Opened.")
    
    def onClose(self):
        print("Closed.")
        
    def proxy_route(self, route:str):
        print("Proxy - Spotify: %s route request" % route)
        return "HELLO"
    
    def start(self):
        print("Spotify started.")