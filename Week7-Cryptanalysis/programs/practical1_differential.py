# Week 7 - Practical Task 1: Differential Cryptanalysis Simulation

sbox = {0:14, 1:4, 2:13, 3:1, 4:15, 5:2, 6:11, 7:8,
        8:3, 9:10, 10:6, 11:12, 12:5, 13:9, 14:0, 15:7}

def encrypt(plaintext, key):
    mixed = plaintext ^ key
    substituted = sbox.get(mixed, mixed)
    bits = format(substituted, '04b')
    permuted = bits[::-1]
    return int(permuted, 2)

def differential_analysis(p1, p2, key):
    print("\n=== Differential Cryptanalysis Simulation ===")
    print("Plaintext 1:", p1)
    print("Plaintext 2:", p2)
    print("Input Difference (XOR):", p1 ^ p2)

    c1 = encrypt(p1, key)
    c2 = encrypt(p2, key)

    print("\nCiphertext 1:", c1)
    print("Ciphertext 2:", c2)
    print("Output Difference (XOR):", c1 ^ c2)

    print("\n--- Analysis ---")
    if (c1 ^ c2) != (p1 ^ p2):
        print("Difference changed after encryption - Good diffusion!")
    else:
        print("Difference unchanged - Weak cipher!")

p1 = int(input("Enter Plaintext 1 (0-15): "))
p2 = int(input("Enter Plaintext 2 (0-15): "))
key = int(input("Enter Key (0-15): "))
differential_analysis(p1, p2, key)
