from rootbunny.extensions.Extension import BaseExtension
from flask import Response, request, send_file
from os import path, listdir
import time, json, uuid

class Extension(BaseExtension):
    def __init__(self, window):
        super().__init__(window)
        
        self.appid = "Spotify"
        
        #@self.event(self.BaseExtensionEvent.ONLOAD_EVENT)
        #def route():
            #self.window.load('https://open.spotify.com')
        #print(self.window.window.get_cookies())
        
        self.window.register_app("Spotify", 1, self.appid, None, self.onOpen, self.onClose)
        self.request_server_bindings([
            '/apps/spotify',
            '/apps/spotify/main.js',
            '/apps/spotify/car.css',
            '/apps/spotify/sdk/premify-player.js',
            '/apps/spotify/sdk/Player/API.js'
        ])
        
        @self.window.Server.route('/apps/spotify/api/v1/player/songs/info')
        @self.window.Server.route('/apps/spotify/api/v1/player/songs/info/')
        def songsinfoapi():
            global songId, songData
            songId = request.headers.get('sid')
            songData = {}
            if not songId:
                return {'error': 'Invalid arguments.'}
            
            if path.exists('./content/extensions/Spotify_idxx9184238x/songs/info/{}.json'.format(str(songId))):
                songData = json.load(open('./content/extensions/Spotify_idxx9184238x/songs/info/{}.json'.format(str(songId))))
                
            return songData
        
        @self.window.Server.route('/apps/spotify/api/v1/player/songs/stream')
        @self.window.Server.route('/apps/spotify/api/v1/player/songs/stream/')
        def songsstreamapi():
            global songData, songId
            songId = request.headers.get('sid')
            songData = {}
            
            if path.exists('./content/extensions/Spotify_idxx9184238x/songs/info/{}.json'.format(str(songId))):
                songData = json.load(open('./content/extensions/Spotify_idxx9184238x/songs/info/{}.json'.format(str(songId))))
            
            print("Now streaming: {}".format(songData.get('description')))
            
            # get the audio
            if path.exists('./content/extensions/Spotify_idxx9184238x/songs/{}.mp3'.format(str(songId))):
                print("Audio is available.")
                return send_file(f"./content/extensions/Spotify_idxx9184238x/songs/{songId}.mp3")
            if path.exists('./content/extensions/Spotify_idxx9184238x/songs/{}.webm'.format(str(songId))):
                print("Audio (WEBM) is available.")
                return send_file(f"./content/extensions/Spotify_idxx9184238x/songs/{songId}.webm")
            
        @self.window.Server.route('/apps/spotify/api/v1/player/songs/stream/less')
        @self.window.Server.route('/apps/spotify/api/v1/player/songs/stream/less/')
        def songsstreamapi_lesssec():
            global songData, songId
            songId = request.args.get('sid')
            songData = {}
            
            if path.exists('./content/extensions/Spotify_idxx9184238x/songs/info/{}.json'.format(str(songId))):
                songData = json.load(open('./content/extensions/Spotify_idxx9184238x/songs/info/{}.json'.format(str(songId))))
            
            print("Now streaming: {}".format(songData.get('description')))
            
            # get the audio
            if path.exists('./content/extensions/Spotify_idxx9184238x/songs/{}.mp3'.format(str(songId))):
                print("Audio is available.")
                return send_file(f"./content/extensions/Spotify_idxx9184238x/songs/{songId}.mp3")
            if path.exists('./content/extensions/Spotify_idxx9184238x/songs/{}.webm'.format(str(songId))):
                print("Audio (WEBM) is available.")
                return send_file(f"./content/extensions/Spotify_idxx9184238x/songs/{songId}.webm")
        
        @self.window.Server.route('/apps/spotify/api/v1/player/songs/total')
        @self.window.Server.route('/apps/spotify/api/v1/player/songs/total/')
        def songs_total_api_v1():
            count = 0
            for i in listdir('./content/extensions/Spotify_idxx9184238x/songs/'):
                if i.endswith('.mp3') or i.endswith('.ogg') or i.endswith('.webm') or i.endswith('.mp4') or i.endswith('.wav'):
                    count+=1
            
            return {'song_count': count}, 200
        
        @self.window.Server.route('/apps/spotify/api/v1/player/songs/search')
        @self.window.Server.route('/apps/spotify/api/v1/player/songs/search/')
        def songs_search_api_v1():
            q = request.headers.get('q','')
            max_results = request.headers.get('m',-1)
            start = request.headers.get('s',0)
            it = 0
            matches = []
            
            for i in listdir('./content/extensions/Spotify_idxx9184238x/songs/info'):
                it += 1
                if it >= start:
                    r = json.load(open(path.join('./content/extensions/Spotify_idxx9184238x/songs/info',i)))
                    if q.lower() in r.get('description','').lower():
                        matches.append({ 'song_info': { 'description': r.get('description'), 'artist': r.get('artist') }, 'index': int(i.split('.',1)[0]), 'matches': 'description' })
                        continue
                    if q.lower() in r.get('artist','').lower():
                        matches.append({ 'song_info': { 'description': r.get('description'), 'artist': r.get('artist') }, 'index': int(i.split('.',1)[0]), 'matches': 'artist' })
                        continue
                if len(matches) >= max_results:
                    break
                    
            return matches
        
    def onOpen(self):
        print("Opened.")
    
    def onClose(self):
        print("Closed.")
        
    def proxy_route(self, route:str):
        print("Proxy - Spotify: %s route request" % route)
        if route.lower() == "apps/spotify".lower():
            return open('./content/extensions/Spotify_idxx9184238x/index.html').read()
        if route.lower() == "apps/spotify/main.js".lower():
            data = open('./content/extensions/Spotify_idxx9184238x/main.js').read()
            return Response(data, mimetype="text/javascript")
        if route.lower() == "apps/spotify/car.css".lower():
            data = open('./content/extensions/Spotify_idxx9184238x/car.css').read()
            return Response(data, mimetype="text/css")
        if route.lower() == "apps/spotify/sdk/premify-player.js".lower():
            data = open('./content/extensions/Spotify_idxx9184238x/sdk/premify-player.js').read()
            return Response(data, mimetype="text/javascript")
        if route.lower() == "apps/spotify/sdk/Player/API.js".lower():
            data = open('./content/extensions/Spotify_idxx9184238x/sdk/Player/API.js').read()
            return Response(data, mimetype="text/javascript")
    
    def start(self):
        print("Spotify started.")