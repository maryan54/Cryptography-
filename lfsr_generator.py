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

seed = 0b1011
taps = [3, 1]
length = 20

sequence = lfsr(seed, taps, length)
print("LFSR Seed:", bin(seed))
print("Taps:", taps)
print("Generated Sequence:", sequence)
print("Sequence Length:", len(sequence))
