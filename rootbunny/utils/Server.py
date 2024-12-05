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
                            try: 
                                response = e.proxy_route(path)
                                if response:
                                    return response
                                else: return "<mark style='color: red; font-weight: 600;'>Critical Error</mark><br/><br/>The application '%s' did not respond to this request.<style>html{background: #111;color:white;}</style>" % (e.appid)
                            except Exception as e:
                                return "Unknown error has occurred, please try again later.<br><br><mark style='background: red; border-radius: 4px; padding: 4px; font-weight: 600; color: white;'>%s</mark><style>html{background: #111;color:white;}</style>" % (e)
            return "ERROR: Proxy route invalid.", 404
        
    def start(self):
        threading.Thread(target=lambda: self.run(port=4000, debug=True, use_reloader=False)).start()