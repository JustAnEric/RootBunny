# RootBunny: a customizable head unit solution in Python
# Currently only supports BusyBox and sway Wayland desktop environment.

# and yes, this was made by Eric

from .unit import Window
from importlib import import_module

import os, threading

print("RootBunny Daemon is starting...")
window = Window()

print("Loading extensions...")

for i in os.listdir('./extensions'):
    if os.path.isfile(os.path.join('./extensions',i)):
        print("Loading extension '%s'..." % i.replace('.py',''))
        mod = import_module(f"extensions.{i.replace('.py','')}", '.').Extension(window)
        threading.Thread(target=mod.start).start()
        window.extensions.append(mod)
        
window.start()