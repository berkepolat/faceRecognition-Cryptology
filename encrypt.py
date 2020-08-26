from tkinter import messagebox
from cryptography.fernet import Fernet
def create_key(keyName):
    key = Fernet.generate_key()
    with open("userkeys/"+keyName+".key", "wb") as file:
        file.write(key)
def open_key(keyName):
    return open("userkeys/"+keyName+".key", "rb").read()
def encrypt(filename,key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        file_data = file.read()
        encrypted_data = f.encrypt(file_data)
        with open(filename, "wb") as file:
            file.write(encrypted_data)
    messagebox.showinfo("Başarılı", filename+" dizinindeki dosya başarıyla şifrelendi.")
def decrypt(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        encrypted_data = file.read()
    try:
        decrypted_data = f.decrypt(encrypted_data)
        messagebox.showinfo("Başarılı", filename + " dizinindeki dosyanın şifresi kaldırıldı.")
    except:
        messagebox.showinfo("Hata", "Bu dosyaya erişminiz engellendi.")
    with open(filename, "wb") as file:
        file.write(decrypted_data)
