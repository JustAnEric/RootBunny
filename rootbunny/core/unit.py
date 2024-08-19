from rootbunny.utils.Server import Server
import webview

class BunnyAPI:
    """This is the Bunny API server, which handles requests from the client."""
    def __init__(self, window: webview.Window, *args, **kwargs) -> None:
        self.window = window
        print("BunnyAPI has been initialized.")

class Window:
    def __init__(self):
        """
        Window constructor. This method constructs a new window and has a few methods that can be used for partial function content to extensions.
        """
        
        self.window = webview.create_window(
            title = "Window"
        )
        self.API = BunnyAPI(self.window)
        self.Server = Server(self.window)
        
        self.Server.start()
        
        self.url = "https://open.spotify.com"
        self.file = "http://localhost:4000/"
        
        self.events = {
            "every_frame": []
        }
        self.extensions = []
        
        self.closed = True
        self.render_state = False
        
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
    
    def _frame(self, window:webview.Window):
        while not self.closed:
            if not self.render_state:
                self.render_state = True
                self.load(self.file)
    
    def _on_closed(self):
        self.closed = True
    
    def start(self):
        self.window.events.closed += self._on_closed
        
        self.closed = False
        webview.start(
            func = self._frame,
            args = (self.window),
            debug = True
        )