P = 149
G = 17

# Rohit's private key
a = 3



# Sunith's private key
b = 6

# Rohit's public key
A = (G**a) % P
print("Rohit's public key is: ", A)

# Sunith's public key
B = (G**b) % P
print("Sunith's public key is: ", B)

# Shared secret
s1 = (B**a) % P
s2 = (A**b) % P

print("Shared secret: ", s1, s2)
