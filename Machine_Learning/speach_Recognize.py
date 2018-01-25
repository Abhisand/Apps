# import pyaudio
# import wave
#
#
# def play_audio(filename):
#     chunk = 1024
#     wf = wave.open(filename,'rb')
#     pa = pyaudio.PyAudio()
#
#     stream = pa.open(
#         format=pa.get_format_from_width(wf.getsampwidth()),
#         channel=wf.getnchannels(),
#         rate=wf.getframerate(),
#         output=True
#     )
#     data_stream = wf.readframes(chunk)
#     while data_stream:
#         stream.write(data_stream)
#         data_stream = wf.readframes(chunk)
#     stream.close()
#     pa.terminate()
#
#
# play_audio("./Audio/abcd.wav")
#
# or



from pygame import mixer # Load the required library

mixer.init()

mixer.music.load('./Audio/hello.mp3')
# while True:
#     mixer.music.play()

import speech_recognition as sr
r = sr.Recognizer()

def initSpeach():
    print("Listening..")
    mixer.music.play()
    with sr.Microphone() as source:
        print("Say Something!")
        audio = r.listen(source)
    mixer.music.play()
    command = ""
    try:
        command = r.recognize_google(audio)
    except:
        print("Couldn't Undurstand u bro...")
    print("Your command")
    print(command)
initSpeach()