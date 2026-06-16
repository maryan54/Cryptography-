# Week 7 - Class Demonstrations: Cryptanalysis

from collections import Counter

# Demo 1: XOR Key Recovery
print("=== Demo 1: XOR Key Recovery ===")
plaintext = 12
key = 5
ciphertext = plaintext ^ key
recovered = ciphertext ^ plaintext
print("Plaintext:", plaintext)
print("Key:", key)
print("Ciphertext:", ciphertext)
print("Recovered Key:", recovered)

# Demo 2: Input Difference
print("\n=== Demo 2: Input Difference ===")
p1 = 10
p2 = 11
difference = p1 ^ p2
print("Plaintext 1:", p1)
print("Plaintext 2:", p2)
print("Difference (XOR):", difference)

# Demo 3: Avalanche Effect
print("\n=== Demo 3: Avalanche Effect ===")
text1 = "HELLO"
text2 = "HELLo"
print("Hash of HELLO:", hash(text1))
print("Hash of HELLo:", hash(text2))

# Demo 4: Frequency Analysis
print("\n=== Demo 4: Frequency Analysis ===")
data = "ABABABABCCCCDDD"
count = Counter(data)
print("Data:", data)
print("Frequency:", count)

# Demo 5: Probability Calculation
print("\n=== Demo 5: Probability ===")
successes = 75
total = 100
probability = successes / total
print("Probability of pattern:", probability)
