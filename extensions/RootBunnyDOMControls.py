from rootbunny.extensions.Extension import BaseExtension
import gpiozero
import webview

class Extension(BaseExtension):
    def __init__(self, window:webview.Window):
        super().__init__(window)
        
        self.appid = "RootBunnyDOM"
        
        # Button bindings
        # self.left = gpiozero.Button(17)
        # self.centre = gpiozero.Button(27)
        # self.right = gpiozero.Button(22)
        # self.top = gpiozero.Button(26)
        # self.bottom = gpiozero.Button(16)
        
        # self.left.when_pressed = self.leftButtonPressed
        # self.centre.when_pressed = self.centreButtonPressed
        # self.right.when_pressed = self.rightButtonPressed
        # self.top.when_pressed = self.topButtonPressed
        # self.bottom.when_pressed = self.bottomButtonPressed
        
    def leftButtonPressed(self):
        print("Left button pressed")
        
    def centreButtonPressed(self):
        print("Centre button pressed")
        
    def rightButtonPressed(self):
        print("Right button pressed")
        
    def topButtonPressed(self):
        print("Top button pressed")
        
    def bottomButtonPressed(self):
        print("Bottom button pressed")
        
    def start(self):
        print("Started core RootBunny dom extension")
        
        
        