import time
import random

def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def lfsr(seed, taps, length):
    state = seed
    sequence = []
    for _ in range(length):
        output = state & 1
        sequence.append(output)
        feedback = 0
        for tap in taps:
            feedback ^= (state >> tap) & 1
        state = (state >> 1) | (feedback << (max(taps)))
    return sequence

print("="*40)
print("ENCRYPTION PERFORMANCE RESULTS")
print("="*40)

# Test Caesar Speed
start = time.time()
for i in range(1000):
    caesar_cipher("HELLO MARYAN", 3)
end = time.time()
print(f"\nCaesar Cipher (1000 runs):")
print(f"Time: {(end-start)*1000:.2f} ms")

# Test LFSR Speed
start = time.time()
for i in range(1000):
    lfsr(0b1011, [3,1], 20)
end = time.time()
print(f"\nLFSR Generator (1000 runs):")
print(f"Time: {(end-start)*1000:.2f} ms")

print("\n" + "="*40)
print("PERFORMANCE TESTING COMPLETE")
print("="*40)
