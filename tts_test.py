import pyttsx3

def main():
    engine = pyttsx3.init()

    # Print available voices
    voices = engine.getProperty("voices")
    print("Available voices:")
    for i, voice in enumerate(voices):
        print(f"{i}: {voice.name}")

    # Try setting Microsoft Zira explicitly
    engine.setProperty("voice", voices[0].id)
    engine.setProperty("rate", 170)

    print("🔊 Speaking now...")
    engine.say("Hello, this is a text to speech test. If you hear my voice, text to speech is working.")
    engine.runAndWait()

    print("✓ Done speaking")

if __name__ == "__main__":
    main()
