import speech_recognition as sphRec

def command():
    takeRecognizer = sphRec.Recognizer()
    with sphRec.Microphone() as source:
        takeRecognizer.adjust_for_ambient_noise(source , duration=1)
        print("Listening...")
        takeRecognizer.pause_threshold = 1
        audio = takeRecognizer.listen(source)

        try:
            print("Recognizing...")
            text = takeRecognizer.recognize_google(audio, language="en-in")
            print(f"User said :{text}\n")
        except Exception as e:
            print(e)
            print("Unable to recognize your voice")

while True:
    command()