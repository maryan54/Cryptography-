# Week 6 - Advanced Task: Multi-Round SPN with Avalanche Demo

sbox = {0:14, 1:4, 2:13, 3:1, 4:15, 5:2, 6:11, 7:8,
        8:3, 9:10, 10:6, 11:12, 12:5, 13:9, 14:0, 15:7}

def substitution(block):
    return sbox.get(block, block)

def permutation(bits):
    return bits[::-1]

def spn_round(value, key, round_num):
    print(f"\n--- Round {round_num} ---")
    mixed = value ^ key
    print("After Key Mixing:", mixed)
    sub = substitution(mixed)
    print("After Substitution:", sub)
    bits = format(sub, '04b')
    perm = permutation(bits)
    print("After Permutation:", perm)
    return int(perm, 2)

def multi_round_spn(plaintext, key, rounds=4):
    value = plaintext
    for r in range(1, rounds + 1):
        value = spn_round(value, key, r)
    return value

print("=== Multi-Round SPN ===")
p1 = int(input("Enter plaintext 1 (0-15): "))
p2 = int(input("Enter plaintext 2 (0-15): "))
key = int(input("Enter key (0-15): "))
rounds = int(input("Number of rounds (e.g. 4): "))

print("\n>>> Encrypting Plaintext 1:")
c1 = multi_round_spn(p1, key, rounds)
print("Ciphertext 1:", c1)

print("\n>>> Encrypting Plaintext 2:")
c2 = multi_round_spn(p2, key, rounds)
print("Ciphertext 2:", c2)

print("\n=== Avalanche Effect ===")
print("Plaintext difference:", p1 ^ p2)
print("Ciphertext difference:", c1 ^ c2)
