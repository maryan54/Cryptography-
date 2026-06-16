# Week 6 Notes - SPN and S-Boxes

## Key Concepts
- SPN = Substitution + Permutation + Key Mixing repeated over rounds
- S-Box introduces non-linearity (confusion)
- Permutation spreads bits (diffusion)
- AES uses SPN structure

## Reflection Answers
1. SPN is a block cipher using substitution, permutation and key mixing per round
2. S-Box improves security by introducing non-linearity
3. Non-linearity prevents algebraic attacks
4. Feistel splits block in half; SPN operates on entire block
5. Permutation spreads bit changes across the block (diffusion)
6. Avalanche effect: small input change = large output change
7. AES uses strong S-Boxes, multiple rounds and high diffusion
