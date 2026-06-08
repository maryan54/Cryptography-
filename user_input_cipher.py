message = input("Enter your message: ")
shift = int(input("Enter shift number: "))

def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

encrypted = caesar_cipher(message, shift)
print("Encrypted:", encrypted)
