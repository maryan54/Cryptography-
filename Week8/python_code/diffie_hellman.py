# ============================================
# BIT4138 - Advanced Cryptography
# Diffie-Hellman Key Exchange Implementation
# Week 8 Practical Task
# ============================================

def is_prime(n):
    """Check if a number is prime"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_prime():
    """Get a valid prime number from user"""
    while True:
        try:
            p = int(input("Enter Public Prime (p): "))
            if is_prime(p):
                return p
            else:
                print(f"  {p} is not a prime number. Try again.")
        except ValueError:
            print("  Please enter a valid number.")

def get_generator(p):
    """Get generator value"""
    while True:
        try:
            g = int(input("Enter Generator (g): "))
            if 1 < g < p:
                return g
            else:
                print(f"  Generator must be between 2 and {p-1}.")
        except ValueError:
            print("  Please enter a valid number.")

def get_private_key(name, p):
    """Get private key from user"""
    while True:
        try:
            key = int(input(f"Enter {name}'s Private Key: "))
            if 1 < key < p:
                return key
            else:
                print(f"  Private key must be between 2 and {p-1}.")
        except ValueError:
            print("  Please enter a valid number.")

def diffie_hellman():
    print("=" * 50)
    print("   Diffie-Hellman Key Exchange Protocol")
    print("   BIT4138 - Advanced Cryptography")
    print("=" * 50)
    print()

    # Step 1: Public Parameters
    print("--- Step 1: Public Parameters ---")
    p = get_prime()
    g = get_generator(p)
    print()

    # Step 2: Private Keys
    print("--- Step 2: Private Keys (Secret) ---")
    alice_private = get_private_key("Alice", p)
    bob_private   = get_private_key("Bob", p)
    print()

    # Step 3: Generate Public Keys
    print("--- Step 3: Generating Public Keys ---")
    alice_public = pow(g, alice_private, p)
    bob_public   = pow(g, bob_private, p)
    print(f"  Alice's Public Key: {g}^{alice_private} mod {p} = {alice_public}")
    print(f"  Bob's   Public Key: {g}^{bob_private} mod {p} = {bob_public}")
    print()

    # Step 4: Exchange
    print("--- Step 4: Exchanging Public Keys ---")
    print(f"  Alice sends Bob:  {alice_public}")
    print(f"  Bob sends Alice:  {bob_public}")
    print()

    # Step 5: Compute Shared Secret
    print("--- Step 5: Computing Shared Secret ---")
    alice_secret = pow(bob_public, alice_private, p)
    bob_secret   = pow(alice_public, bob_private, p)
    print(f"  Alice computes: {bob_public}^{alice_private} mod {p} = {alice_secret}")
    print(f"  Bob computes:   {alice_public}^{bob_private} mod {p} = {bob_secret}")
    print()

    # Step 6: Verify
    print("--- Step 6: Verification ---")
    if alice_secret == bob_secret:
        print(f"  SUCCESS! Shared Secret Key = {alice_secret}")
        print("  Both parties have the same secret key!")
    else:
        print("  ERROR: Secrets do not match!")

    print()
    print("=" * 50)
    print("  Key Exchange Complete!")
    print("=" * 50)

# Run the program
diffie_hellman()
