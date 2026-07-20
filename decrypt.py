from cryptography.fernet import Fernet

with open("secret.key", "rb") as key_file:
    key = key_file.read()

cipher = Fernet(key)

filename = input("Enter encrypted file name: ")

with open(filename, "rb") as file:
    encrypted_data = file.read()

decrypted_data = cipher.decrypt(encrypted_data)

output_file = "decrypted_sample.txt"

with open(output_file, "wb") as file:
    file.write(decrypted_data)

print("File decrypted successfully!")
print("Saved as:", output_file)