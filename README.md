# 🎤 AI Voice Assistant Chatbot

A sophisticated AI-powered voice assistant built with Streamlit that enables natural voice conversations with AI. The assistant listens to your voice, transcribes it, processes your query using a large language model, and responds back with a synthesized voice.

## ✨ Features

- 🎙️ **Voice Recording**: Record your questions using a simple microphone interface
- 📝 **Speech-to-Text**: Powered by Groq's Whisper model for accurate transcription
- 🤖 **AI Processing**: Uses Ollama's DeepSeek model for intelligent responses
- 🔊 **Text-to-Speech**: Natural-sounding voice responses using Edge TTS
- 💬 **Conversation History**: Track all your interactions with timestamps
- 🎨 **User-Friendly Interface**: Clean and intuitive Streamlit UI
- ⚡ **Real-time Processing**: Quick response times with async operations

## 🔄 Processing Pipeline

```
1. 🎙️ Audio Recording
   ↓
2. 📝 Speech-to-Text (Whisper)
   ↓
3. 🤖 LLM Processing (DeepSeek)
   ↓
4. 🔊 Text-to-Speech (Edge TTS)
   ↓
5. ▶️ Play Response
```

## 📋 Prerequisites

Before running the application, ensure you have the following installed:

- **Python 3.12+**
- **Ollama**: Download and install from [ollama.com](https://ollama.com)
- **DeepSeek Model**: Pull the model using `ollama pull deepseek-v3.1:671b-cloud`
- **Groq API Key**: Get your API key from [groq.com](https://groq.com)

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone <your-repository-url>
   cd Ai-voice-assistant
   ```

2. **Create a virtual environment**
   ```bash
   uv venv
   ```

3. **Activate the virtual environment**
   - Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   uv add -r requirements.txt
   ```

5. **Set up environment variables**
   
   Create a `.env` file in the root directory:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   ```

6. **Start Ollama service**
   ```bash
   ollama serve
   ```

7. **Pull the DeepSeek model**
   ```bash
   ollama pull deepseek-v3.1:671b-cloud
   ```

## 🎯 Usage

1. **Run the application**
   ```bash
   streamlit run app.py
   ```

2. **Open your browser**
   
   The app will automatically open at `http://localhost:8501`

3. **Start using the voice assistant**
   - Click "🎙️ Start Recording" to record your question
   - Click "⏹️ Stop Recording" when finished
   - Wait for the AI to process and respond
   - Listen to the audio response

## 📦 Dependencies

- **streamlit**: Web application framework
- **streamlit-mic-recorder**: Audio recording widget
- **groq**: Groq API client for Whisper
- **python-dotenv**: Environment variable management
- **langchain**: LLM framework
- **langchain-ollama**: Ollama integration for LangChain
- **edge-tts**: Text-to-speech synthesis
- **sounddevice**: Audio recording
- **scipy**: Audio processing
- **playsound3**: Audio playback

## 🗂️ Project Structure

```
Ai-voice-assistant/
├── app.py                  # Main Streamlit application
├── requirements.txt        # Python dependencies
├── pyproject.toml         # Project configuration
├── .env                   # Environment variables (not in repo)
├── README.md              # Project documentation
├── human-text.txt         # Transcribed user input
├── llm-text.txt          # LLM response text
├── voice-output.wav      # Recorded audio file
├── audio_output.mp3      # Generated speech response
└── src/                  # Source modules
    ├── audio-recorder.py     # Audio recording module
    ├── speech-to-text.py     # STT module
    ├── llm.py                # LLM processing module
    ├── text-to-speech.py     # TTS module
    └── play-audio.py         # Audio playback module
```

## ⚙️ Configuration

### Voice Settings

The default voice is set to `hi-IN-MadhurNeural` (Hindi voice). To change the voice:

1. Open [app.py](app.py)
2. Find the `VOICE` variable in the `text_to_speech_async` function
3. Replace with your preferred voice from [Edge TTS voices](https://speech.microsoft.com/portal/voicegallery)

### LLM Model

The default model is `deepseek-v3.1:671b-cloud`. To use a different model:

1. Pull the desired model: `ollama pull <model-name>`
2. Update the `model` parameter in the `process_with_llm` function

## 🔧 Troubleshooting

### Ollama Connection Error

**Error**: "Make sure Ollama is running and the model is installed."

**Solution**:
```bash
# Start Ollama service
ollama serve

# Pull the model
ollama pull deepseek-v3.1:671b-cloud
```

### Microphone Access Issues

**Error**: Microphone not working

**Solution**:
- Ensure your browser has microphone permissions enabled
- Check system audio settings
- Try using a different browser (Chrome/Edge recommended)

### API Key Error

**Error**: "Invalid API key"

**Solution**:
- Verify your `.env` file contains the correct Groq API key
- Ensure the key is formatted as: `GROQ_API_KEY=your_key_here`
- Restart the application after updating the `.env` file

## 🎨 Features in Detail

### Conversation History

- All conversations are stored in session state
- View previous interactions with timestamps
- Clear history with a single button click
- Expandable conversation cards for easy navigation

### Auto-play Audio

- Responses automatically play after generation
- Manual playback controls available
- Audio files saved locally for reference

## 🚀 Future Enhancements

- [ ] Support for multiple languages
- [ ] Custom voice selection UI
- [ ] Export conversation history
- [ ] Integration with more LLM providers
- [ ] Wake word detection
- [ ] Conversation context retention
- [ ] Voice customization options

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📧 Contact

For questions or support, please open an issue in the repository.

---

<div align="center">
  <strong>Powered by Groq, Whisper, Ollama, and Edge TTS</strong>
  <br>
  Made with ❤️ using Streamlit
</div>


