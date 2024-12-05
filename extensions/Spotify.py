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
            '/apps/spotify',
            '/apps/spotify/main.js',
            '/apps/spotify/car.css',
            '/apps/spotify/sdk/premify-player.js',
            '/apps/spotify/sdk/Player/API.js'
        ])
        
    def onOpen(self):
        print("Opened.")
    
    def onClose(self):
        print("Closed.")
        
    def proxy_route(self, route:str):
        print("Proxy - Spotify: %s route request" % route)
        if route == "apps/spotify":
            return open('./content/extensions/Spotify_idxx9184238x/index.html').read()
        if route == "apps/spotify/main.js":
            return open('./content/extensions/Spotify_idxx9184238x/main.js').read()
        if route == "apps/spotify/car.css":
            return open('./content/extensions/Spotify_idxx9184238x/car.css').read()
        if route == "apps/spotify/sdk/premify-player.js":
            return open('./content/extensions/Spotify_idxx9184238x/sdk/premify-player.js').read()
        if route == "apps/spotify/sdk/Player/API.js":
            return open('./content/extensions/Spotify_idxx9184238x/sdk/Player/API.js').read()
    
    def start(self):
        print("Spotify started.")