import base64, zlib

def load_encrypted_module(enc_path):
    try:
        with open(enc_path, 'rb') as f:
            data = f.read()
        decoded = zlib.decompress(base64.b64decode(data)).decode()
        exec(decoded, globals())
    except Exception as e:
        print("[ERROR] Failed to load module:", enc_path)
        print("Reason:", e)
