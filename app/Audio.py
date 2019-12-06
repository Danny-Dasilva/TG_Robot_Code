from gtts import gTTS 

class Audio():
    def __init__(self):
        self.previous_string= "none"
    def audio(self, string):
        
        if string != self.previous_string:
            language = 'en'
            
            status = gTTS(text=string, lang=language, slow=False) 
            status.save("/home/mendel/TG_Robot_Code/Audio/status.mp3")
        
        self.previous_string = string