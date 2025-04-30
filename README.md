# InfoSecurity-Proj

# Post-Quantum Cryptography Web Application

A Flask-based web application demonstrating **Kyber512** (NIST-standardized Post-Quantum Cryptography) for secure encryption and decryption. Built with Python, Flask, and Bootstrap.

## Features
- Generate Kyber512 public/private key pairs.
- Encrypt messages using Kyber + AES-256 hybrid encryption.
- Decrypt ciphertexts with matching private keys.
- Responsive UI with error handling.

---

## Prerequisites
- Python 3.6+
- pip (Python package manager)

---

## Installation

1. **Clone the repository**:
   ```bash
   git clone (https://github.com/abdullah-ab00/InfoSecurity-Proj.git)
   cd pqc-web-app

2. Folder Structure

    ├── app.py               # Flask backend routes
   
    ├── crypto.py            # Kyber + AES encryption logic
   
    ├── requirements.txt     # Dependencies
   
    ├── test.py              # Unit tests
   
    ├── Readme.txt           # Readme
   
    ├── /templates
   
    │   ├── index.html       # Homepage
   
    │   └── main.html        # Crypto operations UI
   
    └── /static
        ├── /css             # Bootstrap styles
   
        ├── /fonts           # Fonts
   
        ├── /images          # Imgs
   
        └── /js              # Scripts

---

## Install Dependencies
- pip install -r requirements.txt

---

## Running the Application
- flask run --port 5000 --debug

