from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64
import time

def pad(text):
    while len(text) % 16 != 0:
        text += ' '
    return text

print("="*40)
print("AES PERFORMANCE TESTING")
print("="*40)

key = get_random_bytes(16)
message = "HELLO MARYAN BIT4138"
runs = 1000

# Encryption Performance
start = time.time()
for i in range(runs):
    cipher = AES.new(key, AES.MODE_ECB)
    encrypted = cipher.encrypt(pad(message).encode())
end = time.time()
enc_time = (end - start) * 1000

# Decryption Performance
start = time.time()
for i in range(runs):
    decipher = AES.new(key, AES.MODE_ECB)
    decrypted = decipher.decrypt(encrypted)
end = time.time()
dec_time = (end - start) * 1000

print(f"\nMessage: {message}")
print(f"Key Size: 128 bits")
print(f"Runs: {runs}")
print(f"\nEncryption Time: {enc_time:.2f} ms")
print(f"Decryption Time: {dec_time:.2f} ms")
print(f"Total Time: {enc_time+dec_time:.2f} ms")
print(f"Avg per operation: {(enc_time+dec_time)/runs:.4f} ms")

print("\n" + "="*40)
print("PERFORMANCE TEST COMPLETE")
print("="*40)
