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

def list_target_files(folder_path, allowed_extensions):
    return [
        os.path.join(folder_path, f)
        for f in os.listdir(folder_path)
        if os.path.splitext(f)[1].lower() in allowed_extensions and os.path.isfile(os.path.join(folder_path, f))
    ]
