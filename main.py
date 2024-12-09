import requests
from flask import Flask, render_template, request, jsonify
from api_base import generateResponse

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("home.html")

@app.route("/chatbot", methods=["POST"])
def message():
    try:
        # code to try
        data = request.get_json()
        if data:
            usermesssage = data.get("message", None)
            bot_response = generateResponse(user_message=usermesssage)

        if bot_response.get("error"):
            return jsonify({'message': "Server error"}), 500
        else: 
            bot_text = bot_response['candidates'][0]['content']['parts'][0]["text"]
            print(bot_text)
            return jsonify({'reply': bot_text}), 200
    
    except Exception as e:
        print(e)
        return jsonify({'message': "Server error"}), 500
    
    
if __name__ == "__main__":
    app.run(port=8000, debug=True)
