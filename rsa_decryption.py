import rsa

print("="*40)
print("RSA PRIVATE KEY DECRYPTION")
print("="*40)

# Generate keys
public_key, private_key = rsa.newkeys(1024)

message = "HELLO MARYAN BIT4138"

print(f"\nOriginal Message: {message}")

# Encrypt
encrypted = rsa.encrypt(message.encode(), public_key)
print(f"\nEncrypted (hex):")
print(f"{encrypted.hex()[:50]}...")

# Decrypt with private key
print(f"\nDecrypting with Private Key...")
decrypted = rsa.decrypt(encrypted, private_key).decode()

print(f"\nDecrypted Message: {decrypted}")

# Verify
if message == decrypted:
    print("\nVerification: SUCCESS ✓")
    print("Original matches Decrypted!")
else:
    print("\nVerification: FAILED ✗")

print("\n" + "="*40)
print("DECRYPTION COMPLETE")
print("="*40)
