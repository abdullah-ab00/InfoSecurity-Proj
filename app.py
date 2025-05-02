from flask import Flask, render_template, request, jsonify
from crypto import generate_keys, encrypt_message, decrypt_message
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'supersecretkey')

@app.route("/")
def base():
    return render_template("index.html")

@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/main")
def main():
    return render_template("main.html")

@app.route('/keygen', methods=['POST'])
def handle_keygen():
    try:
        public_key, private_key = generate_keys()
        return jsonify({
            'public': public_key.hex(),
            'private': private_key.hex()
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/encrypt', methods=['POST'])
def handle_encrypt():
    data = request.get_json()
    try:
        ciphertext, _ = encrypt_message(
            data['publicKey'],
            data.get('message', '')
        )
        return jsonify({'ciphertext': ciphertext.hex()})
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/decrypt', methods=['POST'])
def handle_decrypt():
    data = request.get_json()
    try:
        secret = decrypt_message(
            data['privateKey'], 
            data['ciphertext']
        )
        # Return the decrypted string directly
        return jsonify({'secret': secret})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)