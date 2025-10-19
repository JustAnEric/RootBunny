from webview import create_window, windows
from os import path

def openPlayer(url, finishedEvent):
    """
    > DEPRECATED: Use Player class instead.
    """
    
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
            def __init__(h):
                pass
                
            def audioFinished(h):
                if self.onFinishEvent:
                    self.onFinishEvent()
                self.ended = True
                self.window.destroy()
                
            def timeupdate(h, time,outOf):
                if not self.onTimeChangeEvent: return 
                self.onTimeChangeEvent(time,outOf)
        
        self.main = main
        self.url = url
        self.window = create_window(
            title="RootBunny Isolated Player",
            hidden=False,
            html=open("./rootbunny/utils/Audio/background.html",'r').read(),
            transparent=True,
            js_api=Api()
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
        self.window.evaluate_js('document.querySelector(\'audio\').pause();0')
        self.paused = True

    def resume(self):
        self.window.evaluate_js('document.querySelector(\'audio\').play();0')
        self.paused = False

    def togglePP(self):
        if (self.paused):
            self.window.evaluate_js('document.querySelector(\'audio\').play();0')
            self.paused = False
        else:
            self.window.evaluate_js('document.querySelector(\'audio\').pause();0')
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
        document.querySelector('audio').addEventListener('ended', async () => {
            await pywebview.api.audioFinished();
        });
        document.querySelector('audio').addEventListener('timeupdate', async (ev) => {
            await pywebview.api.timeupdate(document.querySelector('audio').currentTime, document.querySelector('audio').duration);
        });
        0
        """ % url)
        
        self.window.hide()

    def close(self):
        self.onFinishEvent()
        self.window.destroy()
        #windows.remove(self.window)
        self.ended = True
        
class Queue:
    def __init__(self, main, initial=[]):
        class Api:
            def __init__(h):
                pass
                
            def audioFinished(h):
                if self.onFinishSongEvent:
                    self.onFinishSongEvent(self.currentSong)
                self.currentSong += 1
                if len(self.queue) <= self.currentSong:
                    self.ended = True
                    self.url = None
                    if self.onFinishQueueEvent: self.onFinishQueueEvent()
                else:
                    self.url = self.queue[self.currentSong]
                
            def timeupdate(h, time,outOf):
                if not self.onTimeChangeEvent: return 
                self.onTimeChangeEvent(time,outOf)
            
        self.main = main
        self.queue = initial
        self.currentSong = 0
        self.url = self.queue[self.currentSong] if len(self.queue) > self.currentSong else None
        self.window = create_window(
            title="RootBunny Isolated Player (Queue)",
            hidden=False,
            html=open("./rootbunny/utils/Audio/background.html",'r').read(),
            transparent=True,
            js_api=Api()
        )
        if not self.url:
            self.paused = True
        else:
            self.paused = False
        self.ended = False
        self.onFinishSongEvent = None
        self.onFinishQueueEvent = None
        self.onTimeChangeEvent = None
        
    def onFinishQueue(self, call):
        self.onFinishQueueEvent = call
    
    def onFinishSong(self, call):
        self.onFinishSongEvent = call

    def onTimeChange(self, call):
        self.onTimeChangeEvent = call
        
    def pause(self):
        self.window.evaluate_js('document.querySelector(\'audio\').pause();0')
        self.paused = True

    def resume(self):
        self.window.evaluate_js('document.querySelector(\'audio\').play();0')
        self.paused = False

    def togglePP(self):
        if (self.paused):
            self.window.evaluate_js('document.querySelector(\'audio\').play();0')
            self.paused = False
        else:
            self.window.evaluate_js('document.querySelector(\'audio\').pause();0')
            self.paused = True
        
    def propagate(self):
        if self.currentSong == 0 and len(self.queue) > 0 and self.paused:
            self.url = self.queue[self.currentSong]
            self.paused = False
            self.window.evaluate_js('document.querySelector(\'audio\').src = "%s";document.querySelector(\'audio\').play();0' % (self.url))
        
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
        document.querySelector('audio').addEventListener('ended', async () => {
            await pywebview.api.audioFinished();
        });
        document.querySelector('audio').addEventListener('timeupdate', async (ev) => {
            await pywebview.api.timeupdate(document.querySelector('audio').currentTime, document.querySelector('audio').duration);
        });
        0
        """ % url)
        
        self.window.hide()

    def close(self):
        self.onFinishQueueEvent()
        self.window.destroy()
        #windows.remove(self.window)
        self.ended = True