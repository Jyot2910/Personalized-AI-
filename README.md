# Personalized-AI-
🌸 Rashi AI – Smart Voice & Text Assistant

Rashi AI is a modern desktop assistant that supports both text-based and voice-based interaction. It combines Speech-to-Text (STT), Text-to-Speech (TTS), and a beautiful GUI to create a smooth conversational experience.

✨ Features
💬 Text Chat Mode – Ask questions and get instant responses
🎤 Voice Input (STT) – Speak and convert your voice into text
🔊 Text-to-Speech (TTS) – AI responses are spoken aloud
🎨 Modern GUI – Built with customtkinter for a sleek UI
⚡ Fast & Responsive – Optimized microphone listening and processing
🛠️ Tech Stack
Python 🐍
SpeechRecognition – Speech-to-text
pyttsx3 – Text-to-speech
pyaudio – Microphone input
customtkinter – GUI framework
google-genai – AI response generation
python-dotenv – Environment variable management
📁 Project Structure
.
├── stt.py                  # Speech-to-Text logic
├── tts.py                  # Text-to-Speech logic
├── tts_test.py             # TTS testing script
├── tempCodeRunnerFile.py   # GUI (Rashi AI app)
├── requirements.txt        # Dependencies
⚙️ Installation
1. Clone the repository
git clone https://github.com/your-username/rashi-ai.git
cd rashi-ai
2. Install dependencies
pip install -r requirements.txt
3. Install PyAudio (Important)

For Windows:

pip install pipwin
pipwin install pyaudio
🚀 Usage
▶️ Run the GUI
python tempCodeRunnerFile.py
🎤 Test Speech Recognition
python stt.py
🔊 Test Text-to-Speech
python tts_test.py
🎯 How It Works
🎤 Speech-to-Text (stt.py)
Uses microphone input
Adjusts for ambient noise
Converts speech → text using Google API
🔊 Text-to-Speech (tts.py)
Uses pyttsx3 engine
Selects Microsoft Zira voice
Speaks AI-generated responses
🧠 AI Response
get_answer() function (from app.py) processes user input and generates replies
🖥️ GUI (customtkinter)
Sidebar with mode selection (Text / Voice)
Chat interface
Input box with send button
