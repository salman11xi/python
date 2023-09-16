from cryptography.fernet import Fernet

key = Fernet.generate_key()

f = Fernet(key)

message = b"Bashaka horo"

encrypted = f.encrypt(message)

print("Encrypted:", encrypted)

decrypted = f.decrypt(encrypted)


print("Decrypted:", decrypted)


