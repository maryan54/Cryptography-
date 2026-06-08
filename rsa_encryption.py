import rsa

print("="*40)
print("RSA PUBLIC KEY ENCRYPTION")
print("="*40)

# Generate keys
public_key, private_key = rsa.newkeys(1024)

message = "HELLO MARYAN BIT4138"

print(f"\nOriginal Message: {message}")
print(f"\nEncrypting with Public Key...")

# Encrypt with public key
encrypted = rsa.encrypt(message.encode(), public_key)
encrypted_hex = encrypted.hex()

print(f"\nEncrypted Message (hex):")
print(f"{encrypted_hex[:50]}...")
print(f"\nEncrypted Length: {len(encrypted)} bytes")

print("\n" + "="*40)
print("PUBLIC KEY ENCRYPTION COMPLETE")
print("="*40)
