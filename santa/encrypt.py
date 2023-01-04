import base64

from cryptography.fernet import Fernet

secret_key = 10

# key is generated
key = str(secret_key).encode()
key = base64.urlsafe_b64encode(key + b"a" * (32 - len(key)))

# value of key is assigned to a variable
f = Fernet(key)

# the plaintext is converted to ciphertext
token = f.encrypt(b"Hey bro you are my santa!!")

# display the ciphertext
print(token)

# decrypting the ciphertext
d = f.decrypt(token).decode()

# display the plaintext
print(d)
