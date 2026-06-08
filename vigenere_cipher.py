def vigenere_cipher(text, key, encrypt=True):
    result = ""
    key = key.upper()
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('A')
            if not encrypt:
                shift = -shift
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
            key_index += 1
        else:
            result += char
    return result

message = "HELLO MARYAN"
key = "SECRET"

encrypted = vigenere_cipher(message, key, True)
decrypted = vigenere_cipher(encrypted, key, False)

print("Original: ", message)
print("Key:      ", key)
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
