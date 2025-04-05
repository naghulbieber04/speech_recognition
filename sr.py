import speech_recognition as sr
# Initialize recognizer
recognizer = sr.Recognizer()

# Use microphone as the audio source
with sr.Microphone() as source:
    print("🎤 Say something...")
    audio = recognizer.listen(source)

    try:
        # Recognize speech using Google Web Speech API
        text = recognizer.recognize_google(audio)
        print("📝 You said:", text)
    except sr.UnknownValueError:
        print("❌ Sorry, I could not understand the audio.")
    except sr.RequestError as e:
        print(f"⚠️ Could not request results; {e}")
