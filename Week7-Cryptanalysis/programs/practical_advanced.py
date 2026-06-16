# Week 7 - Advanced Task: Mini Cryptanalysis Toolkit

from collections import Counter

sbox = {0:14, 1:4, 2:13, 3:1, 4:15, 5:2, 6:11, 7:8,
        8:3, 9:10, 10:6, 11:12, 12:5, 13:9, 14:0, 15:7}

def encrypt(plaintext, key):
    mixed = plaintext ^ key
    substituted = sbox.get(mixed, mixed)
    bits = format(substituted, '04b')
    return int(bits[::-1], 2)

def avalanche_test(key):
    print("\n=== Avalanche Effect Test ===")
    differences = []
    for p in range(15):
        c1 = encrypt(p, key)
        c2 = encrypt(p + 1, key)
        diff = bin(c1 ^ c2).count('1')
        differences.append(diff)
        print(f"P={p} vs P={p+1} -> Ciphertext bit differences: {diff}")
    avg = sum(differences) / len(differences)
    print(f"\nAverage bit differences: {avg:.2f}")

def frequency_analysis(ciphertexts):
    print("\n=== Frequency Analysis ===")
    count = Counter(ciphertexts)
    for val, freq in sorted(count.items()):
        print(f"Ciphertext {val}: appears {freq} times")

def statistical_bias(key):
    print("\n=== Statistical Bias ===")
    ciphertexts = [encrypt(p, key) for p in range(16)]
    frequency_analysis(ciphertexts)

print("=== Mini Cryptanalysis Toolkit ===")
key = int(input("Enter key (0-15): "))
avalanche_test(key)
statistical_bias(key)
print("\nAnalysis Complete!")
