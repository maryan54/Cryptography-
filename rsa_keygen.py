import rsa

print("="*40)
print("RSA KEY PAIR GENERATION")
print("="*40)

public_key, private_key = rsa.newkeys(1024)

print(f"\nPublic Key:")
print(public_key.save_pkcs1().decode())
print(f"Private Key:")
print(private_key.save_pkcs1().decode())
print("KEY GENERATION COMPLETE!")
print("="*40)
