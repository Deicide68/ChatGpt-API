from cryptography.fernet import Fernet, InvalidToken

# Load the key from a file
with open("key.txt", "rb") as key_file:
    key = key_file.read()

# Decrypt the secrets file
try:
    with open("secrets.txt.encrypted", "rb") as secrets_file:
        encrypted_data = secrets_file.read()
        f = Fernet(key)
        decrypted_data = f.decrypt(encrypted_data)

    # Parse the secrets file as a dictionary
    secrets = {}
    for line in decrypted_data.splitlines():
        key, value = line.split(b":", 1)
        secrets[key.decode()] = value.decode()

    # Set the API key as an attribute of a module
    import openai
    openai.api_key = secrets["my_api_key"]

except InvalidToken:
    print("Error: Invalid token")

    
