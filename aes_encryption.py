from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

def pad(text):
    while len(text) % 16 != 0:
        text += ' '
    return text

key = get_random_bytes(16)
message = "HELLO MARYAN"
message_padded = pad(message)

cipher = AES.new(key, AES.MODE_ECB)
encrypted = cipher.encrypt(message_padded.encode())
encrypted_b64 = base64.b64encode(encrypted).decode()

decipher = AES.new(key, AES.MODE_ECB)
decrypted = decipher.decrypt(encrypted).decode().strip()

print("="*40)
print("AES ENCRYPTION")
print("="*40)
print(f"Original:  {message}")
print(f"Key (hex): {key.hex()}")
print(f"Encrypted: {encrypted_b64}")
print(f"Decrypted: {decrypted}")
print("="*40)
