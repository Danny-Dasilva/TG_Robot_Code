
# Import the required module for text  
# to speech conversion 
from gtts import gTTS 
import socket    
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
IP = s.getsockname()[0]
s.close()
hostname = socket.gethostname() 
# This module is imported so that we can  
# play the converted audio 
import os 
  

# Language in which you want to convert 
language = 'en'
  
# Passing the text and language to the engine,  
# here we have marked slow=False. Which tells  
# the module that the converted audio should  
# have a high speed 
myhost = gTTS(text=hostname, lang=language, slow=False) 
myIP = gTTS(text=IP, lang=language, slow=False) 
# Saving the converted audio in a mp3 file named 
# welcome  
myhost.save("host.mp3") 
myIP.save("ip.mp3") 
# Playing the converted file 
while True:

    os.system("mplayer host.mp3") 
    os.system("mplayer ip.mp3") 
    os.system("mplayer status.mp3") 

