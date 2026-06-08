import random

sequence = [random.randint(0,1) for _ in range(1000)]

ones = sequence.count(1)
zeros = sequence.count(0)
total = len(sequence)

print("="*40)
print("STATISTICAL RANDOMNESS TESTING")
print("="*40)
print(f"Total bits generated: {total}")
print(f"Ones:  {ones}  ({ones/total*100:.1f}%)")
print(f"Zeros: {zeros} ({zeros/total*100:.1f}%)")

if 45 <= ones/total*100 <= 55:
    print("\nResult: PASS - Good randomness!")
else:
    print("\nResult: FAIL - Poor randomness!")
print("="*40)
