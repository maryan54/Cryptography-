# Week 6 - Class Demonstrations: SPN, S-Box, Permutation

# Demo 1: S-Box substitution
sbox = {0:14, 1:4, 2:13, 3:1}
print("=== Demo 1: S-Box ===")
print("Input 2 -> Output:", sbox[2])

# Demo 2: Permutation
print("\n=== Demo 2: Permutation ===")
data = "ABCD"
permuted = data[2] + data[3] + data[0] + data[1]
print("Original:", data)
print("Permuted:", permuted)

# Demo 3: Substitution + Permutation
print("\n=== Demo 3: Substitution + Permutation ===")
plaintext = "1234"
substituted = "5678"
permuted2 = substituted[::-1]
print("Plaintext:", plaintext)
print("After Substitution:", substituted)
print("After Permutation:", permuted2)

# Demo 4: Key Mixing (XOR)
print("\n=== Demo 4: Key Mixing ===")
plaintext_val = 9
key = 5
mixed = plaintext_val ^ key
print("Plaintext:", plaintext_val)
print("Key:", key)
print("Round Output (XOR):", mixed)

# Demo 5: Avalanche Effect
print("\n=== Demo 5: Avalanche Effect ===")
text1 = "HELLO"
text2 = "HELLo"
print("Hash of HELLO:", hash(text1))
print("Hash of HELLo:", hash(text2))
print("Small change = completely different hash!")
