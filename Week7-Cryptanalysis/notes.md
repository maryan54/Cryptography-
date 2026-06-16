# Week 7 Notes - Block Cipher Cryptanalysis

## Key Concepts
- Cryptanalysis = breaking/evaluating ciphers without the key
- Algebraic attacks: solve equations to recover keys
- Differential cryptanalysis: study how plaintext differences affect ciphertext
- Linear cryptanalysis: find statistical patterns between plaintext/ciphertext/key bits

## Attack Models
- Ciphertext-only: attacker has only ciphertext
- Known plaintext: attacker has plaintext + ciphertext pairs
- Chosen plaintext: attacker picks plaintexts and gets ciphertext
- Chosen ciphertext: attacker picks ciphertext and gets decrypted output

## Reflection Answers
1. Cryptanalysis is the science of breaking cryptographic systems
2. It helps find weaknesses before attackers do
3. Algebraic attacks create equations from encryption operations and solve for the key
4. Differential cryptanalysis compares how input differences affect output
5. Linear cryptanalysis finds statistical approximations between bits
6. Strong S-Boxes prevent algebraic and linear attacks
7. Avalanche effect ensures small changes produce large unpredictable output changes
8. AES uses strong S-Boxes, many rounds and excellent diffusion properties
