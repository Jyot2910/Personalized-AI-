import speech_recognition as sr

def listen() -> str:
    """
    Listen to microphone input and convert to text.
    Returns the recognized text or empty string on failure.
    """
    r = sr.Recognizer()
    
    # Adjust energy threshold for better performance
    r.energy_threshold = 4000
    r.dynamic_energy_threshold = True
    
    with sr.Microphone() as source:
        print("🎤 Listening... (speak now)")
        
        try:
            # Adjust for ambient noise with shorter duration
            r.adjust_for_ambient_noise(source, duration=0.5)
            
            # Listen with timeout
            audio = r.listen(source, timeout=5, phrase_time_limit=10)
            
            print("🔄 Processing...")
            
            # Try Google Speech Recognition
            text = r.recognize_google(audio)
            print(f"You: {text}")
            return text
            
        except sr.WaitTimeoutError:
            print("⏱️ No speech detected (timeout)")
            return ""
        except sr.UnknownValueError:
            print("❌ Could not understand audio")
            return ""
        except sr.RequestError as e:
            print(f"❌ Speech recognition service error: {e}")
            return ""
        except Exception as e:
            print(f"❌ Error: {e}")
            return ""


def test_microphone():
    """Test if microphone is accessible"""
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("✓ Microphone is accessible")
            print(f"Microphone device: {source}")
            return True
    except Exception as e:
        print(f"✗ Microphone test failed: {e}")
        return False


if __name__ == "__main__":
    print("Testing microphone...")
    test_microphone()
    print("\nTesting speech recognition (say something):")
    result = listen()
    if result:
        print(f"Success! Recognized: {result}")
    else:
        print("No speech recognized")