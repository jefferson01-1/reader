import gtts
from playsound import playsound

# make request to google to get synthesis
tts = gtts.gTTS(
    "i suffered but i did, the next minute he sat on my face i tot i was going to smell his anus (so to speak) but he asked me to lick because thats the only way he can come.")

# save the audio file
tts.save("hello.mp3")
playsound("hello.mp3")
