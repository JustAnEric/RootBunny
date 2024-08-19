from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.core.window import Window

# Set the window size (optional)
Window.size = (800, 480)  # Typical resolution for car screens

class AndroidAutoApp(App):
    def build(self):
        # Main layout
        main_layout = BoxLayout(orientation='vertical')

        # Top status bar
        status_bar = BoxLayout(size_hint_y=0.1, padding=10)
        status_bar.add_widget(Label(text='07:49', font_size='24sp', color=(1, 1, 1, 1)))
        status_bar.add_widget(Label(text='85%', font_size='24sp', color=(1, 1, 1, 1)))

        # App grid layout
        app_grid = GridLayout(cols=3, padding=20, spacing=20)

        # Sample app buttons
        app_icons = [
            {'icon': 'path_to_nav_icon.png', 'text': 'Navigation'},
            {'icon': 'path_to_music_icon.png', 'text': 'Music'},
            {'icon': 'path_to_phone_icon.png', 'text': 'Phone'},
            {'icon': 'path_to_messages_icon.png', 'text': 'Messages'},
            {'icon': 'path_to_settings_icon.png', 'text': 'Settings'},
            {'icon': 'path_to_weather_icon.png', 'text': 'Weather'},
            {'icon': 'path_to_calendar_icon.png', 'text': 'Calendar'},
            {'icon': 'path_to_audiobooks_icon.png', 'text': 'Audiobooks'}
        ]

        for app in app_icons:
            btn = Button(
                text=app['text'],
                background_normal=app['icon'],  # Set the button background to the app icon
                background_down=app['icon'],    # Keep the same background when pressed
                text_size=(None, None),
                font_size='20sp'
            )
            app_grid.add_widget(btn)

        # Add status bar and grid layout to main layout
        main_layout.add_widget(status_bar)
        main_layout.add_widget(app_grid)

        return main_layout

if __name__ == '__main__':
    AndroidAutoApp().run()
