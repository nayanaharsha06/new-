from flask import Flask, request, jsonify

app = Flask(__name__)

# User details (for demonstration purposes)
USER_ID = "john_doe_17091999"
EMAIL = "john@xyz.com"
ROLL_NUMBER = "ABCD123"

@app.route('/bfhl', methods=['POST'])
def handle_post():
    try:
        data = request.json.get('data', [])
        
        numbers = [item for item in data if item.isdigit()]
        alphabets = [item for item in data if item.isalpha()]
        highest_lowercase_alphabet = [char for char in alphabets if char.islower()]
        highest_lowercase_alphabet = sorted(set(highest_lowercase_alphabet))[-1:] if highest_lowercase_alphabet else []

        response = {
            "is_success": True,
            "user_id": USER_ID,
            "email": EMAIL,
            "roll_number": ROLL_NUMBER,
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_lowercase_alphabet": highest_lowercase_alphabet
        }
    except Exception as e:
        response = {
            "is_success": False,
            "user_id": USER_ID,
            "error": str(e)
        }
    
    return jsonify(response)

@app.route('/bfhl', methods=['GET'])
def handle_get():
    return jsonify({"operation_code": 1})

if __name__ == '__main__':
    app.run(debug=True)
