import tkinter as tk
from tkinter import filedialog
import encrypt
def encryptFile(username):
    filename=filedialog.askopenfilename()
    #newPath = shutil.copy(folder, '/')
    encrypt.encrypt(filename,encrypt.open_key(username))
    return
def decryptFile(username):
    filename=filedialog.askopenfilename()
    encrypt.decrypt(filename, encrypt.open_key(username))
def logout(window):
    window.destroy()
def openLoginPage(username):
    login=tk.Tk("")
    login.geometry("190x90")
    login.resizable(False,False)
    encryptButton=tk.Button(login,text="Encrypt File",command= lambda: encryptFile(username))
    decryptButton=tk.Button(login,text="Decrypt File",command= lambda: decryptFile(username))
    logoutButton=tk.Button(login, text="Logout", command=lambda: logout(login))
    encryptButton.place(x=20,y=30,in_=login)
    decryptButton.place(x=100,y=30,in_=login)
    logoutButton.place(x=70,y=60,in_=login)
    userLabel=tk.Label(login, text="Aktif Kullanıcı:")
    userLabel.place(x=0, in_=login)
    nameLabel=tk.Label(login, text=username)
    nameLabel.place(x=80,in_=login)
    login.mainloop()
