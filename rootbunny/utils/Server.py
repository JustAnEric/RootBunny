from flask import Flask, render_template as render
import threading, webview

class Server(Flask):
    def __init__(self, window:webview.Window):
        super().__init__(
            import_name='h', 
            static_url_path="/assets", 
            static_folder="rootbunny/assets/", 
            template_folder="rootbunny/renderable"
        )

        @self.route('/', methods=['GET'])
        def index():
            return render('main/main.html')
        
    def start(self):
        threading.Thread(target=lambda: self.run(port=4000, debug=True, use_reloader=False)).start()