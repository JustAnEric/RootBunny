from rootbunny.extensions.Extension import BaseExtension
# DO NOT REMOVE OR EDIT!
# This file handles all DOM events and manipulation.
# It is important to keep this file so that API bindings are created on the client.

class Extension(BaseExtension):
    def __init__(self, window):
        super().__init__(window)
        
    def start(self):
        print("Started core RootBunny extension")