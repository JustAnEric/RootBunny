from flask import Flask, render_template as render
import threading, webview

class Server(Flask):
    def __init__(self, window):
        super().__init__(
            import_name='h', 
            static_url_path="/assets", 
            static_folder="rootbunny/assets/", 
            template_folder="rootbunny/renderable"
        )

        @self.route('/', methods=['GET'])
        def index():
            return render('splashscreen/index.html')
        
        @self.route('/main', methods=['GET'])
        def main():
            return render('main/main.html')
        
        @self.route('/<path:path>', methods=['GET', 'POST'])
        def proxyroutehandler(path):
            print("Rendering proxy route handler under extension for /{}...".format(str(path)))
            for i in window.apps:
                for p in i['path_selectors']:
                    if not p.startswith('/'):
                        if "/"+p.lower() != "/"+str(path).lower():
                            continue
                    else:
                        if p.lower() != "/"+str(path).lower():
                            continue
                    for e in window.extensions:
                        if e.appid == i['extension']:
                            return e.proxy_route(path)
            return "ERROR: Proxy route invalid.", 404
        
    def start(self):
        threading.Thread(target=lambda: self.run(port=4000, debug=True, use_reloader=False)).start()