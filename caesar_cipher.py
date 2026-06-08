def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + shift) % 26 + base
            result += chr(shifted)
        else:
            result += char
    return result

message = "HELLO MARYAN"
shift = 3

encrypted = caesar_cipher(message, shift)
decrypted = caesar_cipher(encrypted, -shift)

print("Original: ", message)
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
