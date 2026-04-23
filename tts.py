import pyttsx3

def speak(text: str):
    try:
        engine = pyttsx3.init()

        # Select Microsoft Zira explicitly
        voices = engine.getProperty("voices")
        for voice in voices:
            if "Zira" in voice.name:
                engine.setProperty("voice", voice.id)
                break

        engine.setProperty("rate", 170)

        print(f"Rashi: {text}")
        engine.say(text)
        engine.runAndWait()

        engine.stop()  # 🔥 CRITICAL on Windows

    except Exception as e:
        print(f"TTS Error: {e}")
