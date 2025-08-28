from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import base64
import io
from Model import respond
from Memory import ChatMemory
from imageProcessor import process
from Converser import TextToSpeech, SpeechToText

app = Flask(__name__)
CORS(app)

mem=ChatMemory(SystemPrompt="You are DelishBot, a friendly and empathetic food delivery support assistant. Always stay polite, professional, and human-like. Be calm, clear, and apologetic when needed. For genuine issues (wrong, missing, damaged, unhygienic), offer a refund and a small complimentary meal. For minor issues (delay, packaging), apologize, reassure, and explain steps to prevent it. Never blame the customer. always de-escalate and leave a positive impression.")

@app.route('/')
def index():
    """Serve the main UI"""
    return render_template('index.html')


@app.route('/convert_to_text', methods=['POST'])
def convert_to_text():
    """
    Handles the Convert_to_text() function called from frontend
    Receives: {audio: base64, image: filename}
    Returns: combined text from audio and image processing
    """
    data = request.get_json()  # Parse JSON body
    audio_base64 = data.get("audio")
    image_name = data.get("image")
    print("Convert_to_text called by js")
    if not audio_base64:
        print("Audio_base64 is None")
        return jsonify({"text": ""}), 400
    
    audio_bytes = base64.b64decode(audio_base64)
    print("Converted base64 to bytes")
    buffer=io.BytesIO(audio_bytes) 
    buffer.name = "audio.webm"
    print("Converted bytes to buffer")
    Output=SpeechToText(buffer)
    print("Converted buffer to text: ",Output)

    if image_name:
        print("image_name is None")
        Output+='\n\n Image Rendered Details: '+process(image_name.split('.')[0])
    print("responding Output: ",Output)
    return jsonify({"text": Output})


@app.route('/respond', methods=['POST'])
def handle_respond():
    """
    Handles the main AI response workflow
    Receives user query and returns AI response with voice
    """
    data = request.get_json()            
    user_query = data['query']
    mem.UserInp(user_input=user_query)
    response = respond(mem.get_context())
    mem.BotResp(bot_response=response)
    voiceBuffer=TextToSpeech(response)
    mp3_buffer = io.BytesIO(voiceBuffer.read())
    b64 = base64.b64encode(mp3_buffer.read()).decode()
    
    return jsonify({"TextOutput": response,"VoiceOutput":b64})


if __name__ == '__main__':
    print("📡 Server running on http://localhost:5000")
    app.run(host='0.0.0.0',port=5000,debug=True,threaded=True)