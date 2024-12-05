# RootBunny: a customizable head unit solution in Python
# Currently only supports BusyBox and sway Wayland desktop environment.

# and yes, this was made by Eric

from .unit import Window
from importlib import import_module

import os, threading, json

config = json.load(open('./config.json'))

print("RootBunny Daemon is starting...")
print()
window = Window()

if config.get('extensions'):
    if config.get('extensions').get('allow'):
        print("Loading extensions...")

        for i in os.listdir('./extensions'):
            if os.path.isfile(os.path.join('./extensions',i)):
                print("Loading extension '%s'..." % i.replace('.py',''))
                try:
                    mod = import_module(f"extensions.{i.replace('.py','')}", '.').Extension(window)
                    threading.Thread(target=mod.start).start()
                    window.extensions.append(mod)
                except Exception as e:
                    print(f"CRITICAL | An extension had an error: {e}")
                    print(f" - Could not start extension: '{i.replace('.py','')}'.")
    else:
        print("Extensions have been disabled. Letting only trusted extensions run...")
        print("(!) Apps that have been bound to an extension will no longer show in the app view.")
        for i in os.listdir('./extensions'):
            if not i == "RootBunny.py" and not i == "RootBunnyDOMControls.py": continue
            if os.path.isfile(os.path.join('./extensions',i)):
                print("Loading extension '%s'..." % i.replace('.py',''))
                try:
                    mod = import_module(f"extensions.{i.replace('.py','')}", '.').Extension(window)
                    threading.Thread(target=mod.start).start()
                    window.extensions.append(mod)
                except Exception as e:
                    print(f"CRITICAL | An extension had an error: {e}")
                    print(f" - Could not start extension: '{i.replace('.py','')}'.")
        
window.start()