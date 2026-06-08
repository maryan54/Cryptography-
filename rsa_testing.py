import rsa
import time

print("="*40)
print("RSA TESTING AND VALIDATION")
print("="*40)

# Test 1 - Key Generation Speed
print("\nTest 1: Key Generation Speed")
start = time.time()
public_key, private_key = rsa.newkeys(1024)
end = time.time()
print(f"1024-bit keys generated in: {(end-start):.2f} seconds")

# Test 2 - Encryption Speed
print("\nTest 2: Encryption Speed")
message = "HELLO MARYAN BIT4138"
start = time.time()
for i in range(10):
    encrypted = rsa.encrypt(message.encode(), public_key)
end = time.time()
print(f"10 encryptions in: {(end-start)*1000:.2f} ms")

# Test 3 - Decryption Speed
print("\nTest 3: Decryption Speed")
start = time.time()
for i in range(10):
    decrypted = rsa.decrypt(encrypted, private_key).decode()
end = time.time()
print(f"10 decryptions in: {(end-start)*1000:.2f} ms")

# Test 4 - Validation
print("\nTest 4: Encryption Validation")
test_messages = [
    "HELLO MARYAN",
    "BIT4138",
    "CRYPTOGRAPHY",
    "KALI LINUX"
]

all_passed = True
for msg in test_messages:
    enc = rsa.encrypt(msg.encode(), public_key)
    dec = rsa.decrypt(enc, private_key).decode()
    status = "PASS ✓" if msg == dec else "FAIL ✗"
    print(f"{msg}: {status}")
    if msg != dec:
        all_passed = False

print("\n" + "="*40)
if all_passed:
    print("ALL TESTS PASSED SUCCESSFULLY!")
else:
    print("SOME TESTS FAILED!")
print("="*40)
