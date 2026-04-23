import tts
import stt
import app
import sys

def main():
    """Main loop for Rashi voice assistant"""

    print("\n" + "="*50)
    print("🤖 RASHI - AI Voice Assistant")
    print("="*50)

    # Test OpenRouter connection
    print("\n📡 Testing OpenRouter API connection...")
    if not app.test_connection():
        print("\n❌ Failed to connect to OpenRouter API.")
        print("Please check your OPENROUTER_API_KEY in .env file")
        return

    # Test microphone
    print("\n🎤 Testing microphone...")
    if not stt.test_microphone():
        print("\n❌ Microphone test failed.")
        print("Please check your microphone connection")
        return

    print("\n" + "="*50)
    print("✓ All systems ready!")
    print("="*50)
    print("\nCommands:")
    print("  - Say 'exit', 'quit', 'stop', or 'bye' to end")
    print("  - Press Ctrl+C to force quit")
    print("\n" + "="*50 + "\n")

    # Initial greeting
    tts.speak("Hello! I am Rashi, your AI assistant. How can I help you today?")

    conversation_count = 0

    try:
        while True:
            query = stt.listen()

            if not query:
                continue

            if query.lower() in ["exit", "quit", "stop", "bye", "goodbye"]:
                tts.speak("Goodbye! Have a wonderful day.")
                break

            print("\n💭 Thinking...")
            reply = app.get_answer(query)

            tts.speak(reply)

            conversation_count += 1
            print(f"\n{'-'*50}\n")

    except KeyboardInterrupt:
        print("\n\n Interrupted by user")
        tts.speak("Shutting down. Goodbye!")

    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        tts.speak("I encountered an error. Shutting down.")

    finally:
        print(f"\n✓ Conversation ended ({conversation_count} interactions)")
        print("Thank you for using Rashi!\n")


if __name__ == "__main__":
    main()