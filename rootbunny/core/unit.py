from rootbunny.utils.Server import Server
import webview

class BunnyAPI:
    """This is the Bunny API server, which handles requests from the client."""
    def __init__(self, window: webview.Window, *args, **kwargs) -> None:
        self.window = window
        print("BunnyAPI has been initialized.")
        
    def get_sdk(self, version: str = None):
        if version == 'sdk_admin':
            return open('./rootbunny/utils/SDKAdmin.js').read()
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
            height = self.ProductionWH1[1]
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
                self.inject(self.API.get_sdk('sdk_admin'))
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