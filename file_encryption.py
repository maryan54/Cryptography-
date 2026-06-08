from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

def pad(text):
    while len(text) % 16 != 0:
        text += ' '
    return text

# Create a sample file
with open('secret.txt', 'w') as f:
    f.write("This is Maryan's secret message!")

# Read the file
with open('secret.txt', 'r') as f:
    content = f.read()

print("="*40)
print("FILE ENCRYPTION DEMONSTRATION")
print("="*40)
print(f"\nOriginal File Content:")
print(f"{content}")

# Encrypt
key = get_random_bytes(16)
cipher = AES.new(key, AES.MODE_ECB)
encrypted = cipher.encrypt(pad(content).encode())
encrypted_b64 = base64.b64encode(encrypted).decode()

# Save encrypted file
with open('secret_encrypted.txt', 'w') as f:
    f.write(encrypted_b64)

print(f"\nEncrypted Content:")
print(f"{encrypted_b64}")

# Decrypt
decipher = AES.new(key, AES.MODE_ECB)
decrypted = decipher.decrypt(encrypted).decode().strip()

print(f"\nDecrypted Content:")
print(f"{decrypted}")
print("\n" + "="*40)
print("FILE ENCRYPTION COMPLETE")
print("="*40)
