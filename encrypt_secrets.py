from cryptography.fernet import Fernet

# Generate a new key and save it to a file
key = Fernet.generate_key()
with open("key.txt", "wb") as key_file:
    key_file.write(key)

# Encrypt the secrets file
with open("secrets.txt", "rb") as secrets_file:
    data = secrets_file.read()
    f = Fernet(key)
    encrypted_data = f.encrypt(data)

# Save the encrypted secrets to a file
with open("secrets.txt.encrypted", "wb") as encrypted_file:
    encrypted_file.write(encrypted_data)
