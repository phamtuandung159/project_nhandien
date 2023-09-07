from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.camera import Camera
from kivy.uix.button import Button
from kivy.uix.label import Label

class CameraApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        self.icon="icon.png"
        self.title="FaceID"
        self.camera = Camera(resolution=(640, 480), play=False)
        
        self.capture_button = Button(text='Bật Camera')
        self.capture_button.bind(on_press=self.toggle_camera)
        
        self.layout.add_widget(self.camera)
        self.layout.add_widget(self.capture_button)
        
        return self.layout

    def toggle_camera(self, instance):
        if self.camera.play:
            self.camera.play = False
            self.capture_button.text = 'Bật Camera'
        else:
            self.camera.play = True
            self.capture_button.text = 'Tắt Camera'

if __name__ == '__main__':
    CameraApp().run()

