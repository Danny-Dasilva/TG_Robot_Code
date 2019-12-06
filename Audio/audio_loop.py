
#!/usr/bin/python3
from gtts import gTTS 
import socket    
import os
from time import sleep
sleep(3)
path = os.path.dirname(os.path.abspath(__file__))
os.chdir('/home/mendel/TG_Robot_Code/Audio')

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
IP = s.getsockname()[0]
s.close()
hostname = socket.gethostname() 

  

# Language in which you want to convert 
language = 'en'
  
# Passing the text and language to the engine,  
# here we have marked slow=False. Which tells  
# the module that the converted audio should  
# have a high speed 

myhost = gTTS(text=hostname, lang=language, slow=False) 
myIP = gTTS(text=IP, lang=language, slow=False) 
status = gTTS(text="none", lang=language, slow=False) 

print(IP)

myhost.save(path + "/host.mp3") 
myIP.save( path + "/ip.mp3") 
status.save( path +  "/status.mp3")
