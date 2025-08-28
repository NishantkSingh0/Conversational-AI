# DelishBot – Conversational AI Food Delivery Support Assistant

DelishBot is an AI-powered customer support assistant designed for food delivery services. It provides friendly, empathetic, and context-aware responses to customer queries through text and voice interactions, while also supporting image-based information processing for a rich user experience.

## Features

✅ AI Chatbot – Context-aware and polite responses using OpenAI GPT model  
✅ Voice Support – Convert speech to text and text to speech for seamless communication  
✅ Image Analysis – Process uploaded images and extract details for better assistance  
✅ Conversation Memory – Maintains recent chat history for contextual replies  
✅ Responsive Web UI – Interactive interface with audio recording and image upload options  

## Tech Stack
* **Backend:** Python, Flask
* **Frontend:** HTML, CSS, JavaScript
* **AI Models:** OpenAI GPT for text, GPT-4o for speech-to-text and text-to-speech
* **Other Tools:** Flask-CORS, dotenv for environment variables

## Project Structure
```
project/
│
├── main.py               # Main application file (Flask server)
├── Model.py              # Core AI logic (DelishBot response generation)
├── Converser.py          # Handles Speech-to-Text and Text-to-Speech conversions
├── Memory.py             # Stores recent chat history for context
├── imageProcessor.py     # Extracts details from uploaded images
│
├── templates/
│   └── index.html        # Frontend UI with HTML, CSS, and JS
│
├── static/               # (Optional) CSS, JS, images
│
├── .env                  # API keys and environment variables
└── requirements.txt      # Python dependencies
```

## How It Works

* User Interaction: The user can type a message, speak via audio, or upload an image.
* Audio & Image Processing:
    * Audio is converted to text using Speech-to-Text.
    * Images are analyzed for descriptive details.
* AI Response: The system sends the conversation context to the OpenAI model for generating an empathetic, human-like response.
* Voice Output: The response is converted back to speech and sent to the user along with the text reply.
* Memory Management: Previous messages are stored to maintain conversation flow.

## Demo User Interaction
[🎥 Watch Demo Video](Sample_User_Interaction.mp4)

## Installation & Setup
1. Clone the repository
```
git clone https://github.com/your-username/delishbot.git
cd delishbot
```
2. Set up environment variables
```
OpenAI=your_openai_api_key
TTS=your_openai_api_key
SST=your_openai_api_key
```
3. Run the Flask app
```
python main.py
```
`Access the app at http://localhost:5000`

## Demo Workflow

* Step 1: Open the web interface
* Step 2: Tell them you query. or upload image.
* Step 3: AI processes the input and responds with text + voice
* Step 4: Continue chatting with context retained

## Future Enhancements

✅ Multi-language support
✅ Advanced image recognition for menu items
✅ Integration with order tracking APIs
✅ Improved UI for better user experience
