# modules/encryption.py

import hashlib
from cryptography.fernet import Fernet
import base64
import os
from core.utils import color

# ========= [KEY MANAGEMENT] ========= #

def generate_key(save_to=None):
    key = Fernet.generate_key()
    if save_to:
        with open(save_to, "wb") as f:
            f.write(key)
        print(color("green", f"[+] Key saved to {save_to}"))
    return key

def load_key(path):
    try:
        with open(path, "rb") as f:
            return f.read()
    except Exception as e:
        print(color("red", f"[!] Failed to load key: {e}"))
        return None

# ========= [MESSAGE ENCRYPTION/DECRYPTION] ========= #

def encrypt_message(message, key):
    try:
        fernet = Fernet(key)
        encrypted = fernet.encrypt(message.encode())
        return encrypted.decode()
    except Exception as e:
        print(color("red", f"[!] Encryption Error: {e}"))
        return None

def decrypt_message(token, key):
    try:
        fernet = Fernet(key)
        decrypted = fernet.decrypt(token.encode())
        return decrypted.decode()
    except Exception as e:
        print(color("red", f"[!] Decryption Error: {e}"))
        return None

# ========= [FILE ENCRYPTION/DECRYPTION] ========= #

def encrypt_file(filepath, key):
    try:
        with open(filepath, "rb") as f:
            data = f.read()
        fernet = Fernet(key)
        encrypted_data = fernet.encrypt(data)
        with open(filepath + ".enc", "wb") as f:
            f.write(encrypted_data)
        print(color("green", f"[+] File encrypted as {filepath}.enc"))
    except Exception as e:
        print(color("red", f"[!] File encryption failed: {e}"))

def decrypt_file(encrypted_path, key):
    try:
        with open(encrypted_path, "rb") as f:
            encrypted_data = f.read()
        fernet = Fernet(key)
        decrypted_data = fernet.decrypt(encrypted_data)
        original_path = encrypted_path.replace(".enc", "")
        with open(original_path, "wb") as f:
            f.write(decrypted_data)
        print(color("green", f"[+] File decrypted as {original_path}"))
    except Exception as e:
        print(color("red", f"[!] File decryption failed: {e}"))

# ========= [HASHING FUNCTIONS] ========= #

def hash_password(password, algo="sha256"):
    try:
        h = getattr(hashlib, algo)()
        h.update(password.encode())
        return h.hexdigest()
    except AttributeError:
        print(color("red", f"[!] Unsupported hashing algorithm: {algo}"))
        return None

def verify_password(password, hashed, algo="sha256"):
    return hash_password(password, algo) == hashed

# ========= [SHOWCASE MODE] ========= #

def demo_encryption():
    print(color("cyan", "\n[ Encryption Demo ]"))
    msg = input(color("green", "Enter message: "))
    key = generate_key()
    enc = encrypt_message(msg, key)
    dec = decrypt_message(enc, key)

    print(color("yellow", f"Encrypted: {enc}"))
    print(color("green", f"Decrypted: {dec}"))

def demo_hash():
    print(color("cyan", "\n[ Hashing Demo ]"))
    password = input(color("green", "Enter password: "))
    hashed = hash_password(password)
    print(color("yellow", f"SHA256: {hashed}"))

# ========= [MAIN FOR DEBUG/ADMIN] ========= #

if __name__ == "__main__":
    print(color("bold_magenta", "\n[ Vampire Encryption Module Tester ]"))
    print(color("cyan", "[1] Encrypt Message\n[2] Decrypt Message\n[3] Encrypt File\n[4] Decrypt File\n[5] Hash Password\n"))

    opt = input(color("green", "[?] Choice: "))
    if opt == "1":
        msg = input("Message: ")
        key = generate_key()
        print("Encrypted:", encrypt_message(msg, key))
    elif opt == "2":
        token = input("Encrypted Token: ")
        key_path = input("Key File Path: ")
        key = load_key(key_path)
        print("Decrypted:", decrypt_message(token, key))
    elif opt == "3":
        path = input("File Path: ")
        key = generate_key()
        encrypt_file(path, key)
    elif opt == "4":
        path = input("Encrypted File Path: ")
        key_path = input("Key File Path: ")
        key = load_key(key_path)
        decrypt_file(path, key)
    elif opt == "5":
        password = input("Password: ")
        print("Hashed:", hash_password(password))
