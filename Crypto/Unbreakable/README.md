Hint:I learned in my cryptography class that One Time Pad is an unbreakable encryption! Good thing I've used it to store my secret. Bet you can't crack it!

We exploit the fact that 
1) m XOR k = c => c XOR k = m
2) We are given sample text and it's output(in output.txt). We XOR them to get key, and XOR that key with our encrypted flag(also in output.txt)

I made a python script for it (decryptorggwp.py)

Flag: TECHWKND{0n3_t1Me_54D_AF_qkm8W}