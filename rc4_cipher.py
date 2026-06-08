def rc4(key, plaintext):
    # Key Scheduling Algorithm (KSA)
    S = list(range(256))
    j = 0
    key = [ord(c) for c in key]
    
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]
    
    # Pseudo-Random Generation Algorithm (PRGA)
    i = j = 0
    result = []
    for char in plaintext:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        k = S[(S[i] + S[j]) % 256]
        result.append(chr(ord(char) ^ k))
    
    return ''.join(result)

key = "SECRET"
message = "HELLO MARYAN"

encrypted = rc4(key, message)
decrypted = rc4(key, encrypted)

print("="*40)
print("RC4 STREAM CIPHER")
print("="*40)
print(f"Key:       {key}")
print(f"Original:  {message}")
print(f"Encrypted: {encrypted.encode()}")
print(f"Decrypted: {decrypted}")
print("="*40)
