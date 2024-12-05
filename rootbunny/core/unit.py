from rootbunny.utils.Server import Server
from rootbunny.utils.Audio.audio import Player as AudioPlayer
import webview, threading

class BunnyAPI:
    """This is the Bunny API server, which handles requests from the client."""
    def __init__(self, window: webview.Window, *args, **kwargs) -> None:
        self.window = window
        print("BunnyAPI has been initialized.")
        
    def get_sdk(self, version: str = None, info: dict = None):
        if version == 'sdk_admin':
            content = open('./rootbunny/utils/SDKAdmin.js').read()
            for key in info:
                value = info[key]
                if "/`"+key+"`/" in content:
                    content = content.replace(f"/`{key}`/", str(value))
            return content
        else:
            return open('./rootbunny/utils/SDK.js').read()
        
class AppInfo:
    def __init__(self, info:dict):
        self.name = info.get('name', None)
        self.version = info.get('version', None)
        
class App:
    def __init__(self, window:webview.Window, app:{dict}) -> None:
        """App constructor. Initializes an application instance."""
        self.window = window
        self.app = app
        
        self.info = AppInfo(app)

class Window:
    def __init__(self) -> None:
        class API:
            def __init__(self):
                print("API START")
                
            def on(s, event:str, *args):
                if event == 'audio:player/open':
                    context : str = args[0]
                    url : str = args[1]
                    functorunonaudiofinish : str = args[2]
                    functorunonaudiotimeupdate : str = args[3]
                    
                    regkeyindex = None

                    # add to audio registry
                    if not (self.registry.get(context)):
                        self.registry[context] = []

                    self.registry[context].append({
                        "volume": 100, # out of 100
                        "playing": True,
                        "playerInstance": None,
                        "context": context,
                        "info": { "mediaSession": {} }
                    })
                    regkeyindex = len(self.registry[context])-1
                    
                    player = AudioPlayer(self.window,url)
                    
                    @player.onFinish
                    def onFinish():
                        self.window.evaluate_js(f"{functorunonaudiofinish}();")
                        del self.registry[context][regkeyindex] # unmount it from the registry
                        #self.registry[context] = self.registry[context].slice((regkeyindex+1))
                        print("Audio finished playing under context '"+context+"' and index "+regkeyindex.toString()+". Unmounted from registry.");
                        print(self.registry[context])

                        message = []
                        if (self.registry[context]):
                            for key in self.registry[context]:
                                message.append({
                                    "volume": key['volume'],
                                    "playing": key['playing'],
                                    "context": key['context'],
                                    "info": key['info']
                                }) #playerInstance is not available.

                        self.window.evaluate_js(('audio.stateChange({"data": %s, "context": %*[]})' % (str(message))).replace('%*[]',str(context)))
                        #return['audio:state_change', {'data': message, 'context': context}]
                        
                    @player.onTimeChange
                    def onTimeUpdate(time, outof):
                        self.window.evaluate_js(f"{functorunonaudiotimeupdate}({time}, {outof})")
                        self.window.evaluate_js(('audio.timeChange({"data": %s, "context": %*[]})' % (str({"time": time, "outof": outof}))).replace('%*[]',str(context)))
                        
                    player.start()

                    self.registry[context][regkeyindex]['playerInstance'] = player
                if event == "interface:apps/open":
                    app_name : str = args[0]
                    app_loaded : bool = False
                    for app in self.apps:
                        if str(app.get('name')) == str(app_name):
                            self.window.load_url(f"{self.file}{app.get('path_selectors')[0]}") # the zeroth item in the path selectors list will be used as it is the entrypoint
                            app_loaded = True
                            if app.get('onOpen') and callable(app.get('onOpen')):
                                threading.Thread(target=app.get('onOpen'), daemon=False).start()
                            print(f"App '{app_name}' has been opened.")
                            break
                    if not app_loaded:
                        print(f"App '{app_name} was not loaded: not found")
                if event == "interface:apps/load/init":
                    uri = self.window.get_current_url()
                    app_path = uri.partition(self.url)[2]
                    sent : bool = False
                    for app in self.apps:
                        # see which app has the path registered
                        if app_path in app.get('path_selectors',[]):
                            # we found the app, send init message
                            cls = app.get('app')
                            cls.init_sent(app_path)
                            sent = True
                            break
                    if not sent:
                        return False
                    else:
                        return True
                pass
        
        """
        Window constructor. This method constructs a new window and has a few methods that can be used for partial function content to extensions.
        """
        
        self.ProductionWH1 = (
            1280, 720
        )
        self.ProductionWH2 = (
            1024, 720
        )
        
        self.window = webview.create_window(
            title = "Window",
            width = self.ProductionWH1[0],
            height = self.ProductionWH1[1],
            js_api=API()
        )
        self.API = BunnyAPI(self.window)
        self.Server = Server(self)
        
        self.Server.start()
        
        self.url = "https://open.spotify.com"
        self.file = "http://localhost:4000/"
        
        self.events = {
            "every_frame": []
        }
        self.extensions = []
        self.apps = []
        self.registry = {}
        
        self.closed = True
        self.render_state = False
        
        self._no_sdk = False
        
    def inject(self, js:str):
        """Injects JavaScript code on the current page. This has no callback function!"""
        return self.window.evaluate_js(js)
    
    def inject_with_callback(self, js:str):
        """Injects JavaScript code on the current page with a callback function."""
        def execu(func):
            return self.window.evaluate_js(js, func)
        return execu
    
    def load(self, url:str):
        """Loads the specified URL on the current window."""
        self.window.load_url(url)
    
    def load_html(self, html:str):
        """Loads the specified HTML on the current window."""
        self.window.load_html(html)
    
    def load_css(self, css:str):
        """Loads the specified CSS on the current window."""
        self.window.load_css(css)
        
    def register_app(self, name:str, version:float, extensionName:str, onOpen=None, onClose=None):
        data = {
            "name": name,
            "version": version,
            "onOpen": onOpen,
            "onClose": onClose,
            "path_selectors": [],
            "extension": extensionName
        }
        app = App(self.window, data)
        data['app'] = app
        self.apps.append(data)
        
        return app
    
    def _frame(self, window:webview.Window):
        window.move(0,0)
        while not self.closed:
            if not self.render_state:
                self.render_state = True
                self._no_sdk = True
                self.load(self.file)
                self.inject(self.API.get_sdk('sdk_admin', { '$START.bool': 'true' }))
                print("Rendered.")
                self._no_sdk = False
    
    def _on_closed(self):
        self.closed = True
        
    def _on_load(self):
        if not self._no_sdk:
            self.inject(self.API.get_sdk())
        print("window.rootbunny Injected RootBunny API..")
    
    def start(self):
        self.window.events.closed += self._on_closed
        self.window.events.loaded += self._on_load
        
        self.closed = False
        webview.start(
            func = self._frame,
            args = (self.window),
            debug = True
        )