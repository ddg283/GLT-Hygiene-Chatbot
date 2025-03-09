from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_input = request.json.get("message")

    responses = {
        "deodorant": "I recommend Brand A (aluminum-free) or Brand B (long-lasting protection).",
        "soap": "Try Brand C (organic) or Brand D (for sensitive skin).",
        "hand sanitizer": "Get alcohol-based sanitizer with moisturizing aloe vera.",
        "order status": "Your order will be delivered in 2 days."
    }

    response = responses.get(user_input.lower(), "I'm sorry, I don't understand that request.")
    
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port
