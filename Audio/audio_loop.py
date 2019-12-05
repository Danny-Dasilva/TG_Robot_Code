
#!/usr/bin/python3
from gtts import gTTS 
import socket    
import os
from time import sleep
sleep(3)
path = os.path.dirname(os.path.abspath(__file__))


# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# s.connect(("8.8.8.8", 80))
# IP = s.getsockname()[0]
# s.close()
# hostname = socket.gethostname() 

  

# # Language in which you want to convert 
# language = 'en'
  
# # Passing the text and language to the engine,  
# # here we have marked slow=False. Which tells  
# # the module that the converted audio should  
# # have a high speed 
# myhost = gTTS(text=hostname, lang=language, slow=False) 
# myIP = gTTS(text=IP, lang=language, slow=False) 
# status = gTTS(text="none", lang=language, slow=False) 

# # Saving the converted audio in a mp3 file named 
# # welcome  
# myhost.save(path + "/host.mp3") 
# myIP.save( path + "/ip.mp3") 
# # status.save( path +  "/status.mp3")

# # Playing the converted file 
while True:
    print(path)
    os.system("mplayer " + path +  "/host.mp3") 
    os.system("mplayer " + path +  "/ip.mp3") 
    os.system("mplayer " + path +   "/status.mp3") 

