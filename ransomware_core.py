from cryptography.fernet import Fernet
import os

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("secret.key", "rb").read()

def encrypt_file(file_path, key):
    fernet = Fernet(key)
    with open(file_path, "rb") as file:
        data = file.read()
    encrypted = fernet.encrypt(data)
    with open(file_path, "wb") as file:
        file.write(encrypted)

def decrypt_file(file_path, key):
    fernet = Fernet(key)
    with open(file_path, "rb") as file:
        data = file.read()
    try:
        decrypted = fernet.decrypt(data)
        with open(file_path, "wb") as file:
            file.write(decrypted)
        return True
    except Exception:
        return False

# Updated to include recursive file scanning
def list_target_files(folder_path, allowed_extensions):
    matched_files = []
    for root, _, files in os.walk(folder_path):
        for file in files:
            if os.path.splitext(file)[1].lower() in allowed_extensions:
                matched_files.append(os.path.join(root, file))
    return matched_files
