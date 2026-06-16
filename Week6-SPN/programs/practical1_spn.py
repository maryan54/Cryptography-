# Week 6 - Practical Task 1: Basic SPN Design

sbox = {0:14, 1:4, 2:13, 3:1, 4:15, 5:2, 6:11, 7:8,
        8:3, 9:10, 10:6, 11:12, 12:5, 13:9, 14:0, 15:7}

def substitution(block):
    return sbox.get(block, block)

def permutation(bits):
    return bits[::-1]

def spn_encrypt(plaintext, key):
    print("\n--- SPN Encryption ---")
    print("Plaintext:", plaintext)

    # Round 1
    mixed = plaintext ^ key
    print("After Key Mixing:", mixed)

    substituted = substitution(mixed)
    print("After Substitution:", substituted)

    bits = format(substituted, '04b')
    permuted = permutation(bits)
    print("After Permutation:", permuted)

    # Round 2
    mixed2 = int(permuted, 2) ^ key
    print("\nRound 2 - After Key Mixing:", mixed2)

    substituted2 = substitution(mixed2)
    print("Round 2 - After Substitution:", substituted2)

    bits2 = format(substituted2, '04b')
    permuted2 = permutation(bits2)
    print("Round 2 - After Permutation:", permuted2)

    ciphertext = int(permuted2, 2)
    print("\nFinal Ciphertext:", ciphertext)
    return ciphertext

plaintext = int(input("Enter plaintext (0-15): "))
key = int(input("Enter key (0-15): "))
spn_encrypt(plaintext, key)
