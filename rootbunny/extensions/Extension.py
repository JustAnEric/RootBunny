from rootbunny.core.rootbunny import Window

class BaseExtension:
    class BaseExtensionEvent:
        events = {}
        ONLOAD_EVENT = 0
        ONCLOSE_EVENT = 1
        DOM_EVENT = 2
        RENDER_EVENT = 3
        
        class RealEvent:
            def IsA(obj:object, event):
                ev = BaseExtension.BaseExtensionEvent
                if event == ev.ONLOAD_EVENT and ev.ONLOAD_EVENT == obj:
                    return True
                if event == ev.ONCLOSE_EVENT and ev.ONCLOSE_EVENT == obj:
                    return True
                if event == ev.DOM_EVENT and ev.DOM_EVENT == obj:
                    return True
                if event == ev.RENDER_EVENT and ev.RENDER_EVENT == obj:
                    return True
                return False
    
    def __init__(self, window):
        self.window = window
        self.window : Window
        self.events = {'load':[],'close':[]}
        
    def event(self, h:BaseExtensionEvent.RealEvent):
        def t_(func):
            if h == self.BaseExtensionEvent.ONLOAD_EVENT:
                self.window.window.events.loaded += func
                self.events['load'].append(func)
            if h == self.BaseExtensionEvent.ONCLOSE_EVENT:
                self.window.window.events.closing += func
                self.events['close'].append(func)
        return t_
        