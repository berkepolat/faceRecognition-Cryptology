import tkinter as tk
import recognition
root = tk.Tk("Encrypter")
root.geometry("190x90")
root.resizable(False, False)
tk.Label(root, text="Username").grid(row=0)
tk.Label(root, text="Password").grid(row=1)
user = tk.Entry(root)
pw = tk.Entry(root)
user.grid(row=0, column=1)
pw.grid(row=1, column=1)
buttonLogin = tk.Button(root, text="Login", command=lambda: recognition.login(user.get(), pw.get()))
buttonLogin.place(x=38, y=50, in_=root)
buttonRegister = tk.Button(root, text="Register", command=lambda: recognition.register(user.get(), pw.get()))
buttonRegister.place(x=104, y=50, in_=root)

