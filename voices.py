import gtts
from playsound import playsound

jeff = input("enter text: ")
print(jeff)
# make request to google to get synthesis
tts = gtts.gTTS(jeff)

# save the audio file
tts.save("hello.mp3")
playsound("hello.mp3")
