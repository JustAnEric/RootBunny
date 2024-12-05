from webview import create_window
from os import path

def openPlayer(url, finishedEvent):
    class Api:
        def getAudio(self):
            return url
        
        def audioFinished(self):
            finishedEvent()
            win.destroy()
    
    win = create_window(
        title="RootBunny Isolated Player",
        hidden=True,
        url="./rootbunny/utils/Audio/background.html",
        transparent=True,
        js_api=Api()
    )
    win.hide()
    
    def create_sdk(f:str):
        return open(f'./rootbunny/utils/Audio/{f}.js','r').read()
    
    win.evaluate_js(create_sdk('inbuilt-sdk'))

class Player:
    def __init__(self, main, url):
        class Api:
            def audioFinished():
                if self.onFinishEvent:
                    self.onFinishEvent()
                self.ended = True
                self.window.destroy()
                
            def timeupdate(time,outOf):
                if not self.onTimeChangeEvent: return 
                self.onTimeChangeEvent(time,outOf)
        
        self.main = main
        self.url = url
        self.window = create_window(
            title="RootBunny Isolated Player",
            hidden=False,
            html=open("./rootbunny/utils/Audio/background.html",'r').read(),
            transparent=True,
            js_api=Api
        )
        self.paused = False
        self.ended = False
        self.onFinishEvent = None
        self.onTimeChangeEvent = None

        #self.window.hide()

    def onFinish(self, call):
        self.onFinishEvent = call

    def onTimeChange(self, call):
        self.onTimeChangeEvent = call

    def pause(self):
        self.window.evaluate_js('audio.pause();0')
        self.paused = True

    def resume(self):
        self.window.evaluate_js('audio.play();0')
        self.paused = False

    def togglePP(self):
        if (self.paused):
            self.window.evaluate_js('audio.play();0')
            self.paused = False
        else:
            self.window.evaluate_js('audio.pause();0')
            self.paused = True

    def start(self):
        url = self.url
        
        def create_sdk(f:str):
            return open(f'./rootbunny/utils/Audio/{f}.js','r').read()
    
        self.window.evaluate_js(create_sdk('inbuilt-sdk'))

        self.window.evaluate_js("""
        document.querySelector('audio').src = "%s";
        //document.querySelector('audio').load();
        //document.querySelector('audio').onload = function(ev) {
        document.querySelector('audio').play();
        //};0
        0
        """ % url)
        
        self.window.hide()

    def close(self):
        self.onFinishEvent()
        self.window.destroy()
        self.ended = True