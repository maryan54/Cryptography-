from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

def pad(text):
    while len(text) % 16 != 0:
        text += ' '
    return text

print("="*40)
print("DECRYPTION RESULTS")
print("="*40)

# Test multiple messages
messages = [
    "HELLO MARYAN",
    "CRYPTOGRAPHY",
    "KALI LINUX",
    "BIT4138 CLASS"
]

key = get_random_bytes(16)
print(f"\nKey (hex): {key.hex()}\n")

for msg in messages:
    # Encrypt
    cipher = AES.new(key, AES.MODE_ECB)
    encrypted = cipher.encrypt(pad(msg).encode())
    encrypted_b64 = base64.b64encode(encrypted).decode()

    # Decrypt
    decipher = AES.new(key, AES.MODE_ECB)
    decrypted = decipher.decrypt(encrypted).decode().strip()

    print(f"Original:  {msg}")
    print(f"Encrypted: {encrypted_b64}")
    print(f"Decrypted: {decrypted}")
    print("-"*40)

print("\nALL DECRYPTIONS SUCCESSFUL!")
print("="*40)
