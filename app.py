from flask import Flask, render_template, request, jsonify
import secrets

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_password', methods=['POST'])
def generate_password():
    password_length = int(request.form.get('length'))
    special_chars = request.form.get('special_chars') == 'true'
    numbers = request.form.get('numbers') == 'true'
    exclude_special_chars = request.form.get('exclude_special_chars') == 'true'
    
    password_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if special_chars:
        password_characters += "!@#$%^&*()-_=+[]{}|;:,.<>?/~"
    if numbers:
        password_characters += "0123456789"
    if exclude_special_chars:
        password_characters = password_characters.replace("!@#$%^&*(){}[]|;:,.<>?/~", "")

    secure_random = secrets.SystemRandom()
    generated_password = ''.join(secure_random.choice(password_characters) for _ in range(password_length))
    
    return jsonify({'password': generated_password})

if __name__ == '__main__':
    app.run(debug=True)
