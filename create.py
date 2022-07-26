# # # Import the required module for text
# # # to speech conversion
from gtts import gTTS

# # # This module is imported so that we can
# # # play the converted audio
import os
from materials import CVCU
# # # The text that you want to convert to audio


# # # Language in which you want to convert
language = 'en'

# # # Passing the text and language to the engine,
# # # here we have marked slow=False. Which tells
# # # the module that the converted audio should
# # # have a high speed
for i in CVCU:
    
    
    myobj = gTTS(text=i.lower(), lang=language, slow=True)

#         # Saving the converted audio in a mp3 file named
#         # welcome
    myobj.save(f"src/phase4/short/u/{i.lower()}.mp3")

# # # Playing the converted file
# # #os.system("mpg321 welcome.mp3")
