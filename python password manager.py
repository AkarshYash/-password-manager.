pip install cryptography

import sys
import getpass
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend

def generate_key(password):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=b'salt',
        iterations=100000,
        backend=default_backend()
    )
    return base64.urlsafe_b64encode(kdf.derive(password))

def load_credentials(key):
    try:
        with open('credentials.enc', 'rb') as f:
            encrypted_data = f.read()
        fernet = Fernet(key)
        return fernet.decrypt(encrypted_data)
    except (IOError, OSError, FernetError):
        return None

def save_credentials(key, credentials):
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(credentials)
    with open('credentials.enc', 'wb') as f:
        f.write(encrypted_data)

def main():
    if len(sys.argv) != 2:
        print("Usage: python password_manager.py [add|get]")
        return

    action = sys.argv[1]

    if action == 'add':
        password = getpass.getpass("Enter a new password: ")
        key = generate_key(password.encode())
        save_credentials(key, password.encode())
        print("Password saved.")

    elif action == 'get':
        password = getpass.getpass("Enter your password: ")
        key = generate_key(password.encode())
        loaded_credentials = load_credentials(key)

        if loaded_credentials is None:
            print("No saved credentials found.")
        else:
            print("Retrieved password:", loaded_credentials.decode())

    else:
        print("Invalid action. Use 'add' or 'get'.")

if _name_ == '_main_':
    main()
    
    
    python password_manager.py add
python password_manager.py get