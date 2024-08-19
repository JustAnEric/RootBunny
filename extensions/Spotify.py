from rootbunny.extensions.Extension import BaseExtension

class Extension(BaseExtension):
    def __init__(self, window):
        super().__init__(window)
        
        #@self.event(self.BaseExtensionEvent.ONLOAD_EVENT)
        #def route():
            #self.window.load('https://open.spotify.com')
        #print(self.window.window.get_cookies())
    
    def start(self):
        print("Spotify started.")