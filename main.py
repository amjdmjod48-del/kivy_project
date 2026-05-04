from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from plyer import vibrator
from plyer import notification
from plyer import camera
import webbrowser
from jnius import autoclass



PythonActivity = autoclass('org.kivy.android.PythonActivity')
Intent = autoclass('android.content.Intent')
MediaStore = autoclass('android.provider.MediaStore')


class MyApp(App):
    def build(self):
       box = BoxLayout()
       self.counter =0
       
       
       
       
       self.counter_button = Button(text ='click to plus number >> ', font_size = 30, background_color = (1,0,0,1))
       
       self.google_button = Button(text ='open google', font_size = 30, background_color = (0,1,0,1))
       self.camera_button= Button(text = 'open camera', font_size = 30, background_color = (0,0,1,1))
       self.counter_button.bind(on_press = self.increment)
       self.google_button.bind(on_press = self.open_google)
       self.camera_button.bind(on_press = self.open_camera)
       box.add_widget(self.counter_button)
       box.add_widget(self.google_button)
       box.add_widget(self.camera_button)
       return box
    def increment(self, instance):
        self.counter +=1
    
        self.counter_button.text=f'click to plus number >> {self.counter}'
        #vibrator.vibrate(0.1)
        notification.notify(title='app',message=f'app is {self.counter}', timeout=1)
    def open_google(self, instance):
       
        webbrowser.open('https://www.google.com')    

    def open_camera(self,instance):
       
       intent = Intent(MediaStore.ACTION_IMAGE_CAPTURE)

       currentActivity = PythonActivity.mActivity
       currentActivity.startActivity(intent)
                    
        
    


MyApp().run()