from cryptography.fernet import Fernet
with open("secret.key", "rb") as key_file:
    key = key_file.read()
cipher = Fernet(key)
filename = input("Enter file name to encrypt: ")
with open(filename, "rb") as file:
    data = file.read()
encrypted_data = cipher.encrypt(data)
with open("decrypted_sample.txt", "wb") as file:
    file.write(decrypted_data)
print("File encrypted successfully!")