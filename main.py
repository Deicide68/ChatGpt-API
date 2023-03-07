from cryptography.fernet import Fernet, InvalidToken
from termcolor import colored
from getpass import getpass
import openai

# Generate text using GPT-3

messages=[
            {"role": "system", "content": "You are a helpful assistant."},
        ]

def generate_text(user_message):
    messages.append(user_message)
    response = openai.ChatCompletion.create(
        messages=messages,
        model="gpt-3.5-turbo",
    )
    message = ''
    for choice in response.choices:
        message += choice.message.content
    system_message = {"role": "assistant", "content": message}
    messages.append(system_message)
    return message


# Load the key from a file
with open("E:/temp/ChatGpt-API/key.txt", "rb") as key_file: 
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
    openai.api_key = secrets["my_api_key"]

    while(True):
      print()
      # input = colored((getpass(prompt="Input: ")), "blue")
      user_message = {"role": "user", "content": input("Input: ")}

      response = generate_text(user_message)

      print()
      print(colored(response, "blue"))
      print()


except InvalidToken:
    print(colored("Error: Invalid token", "red"))
