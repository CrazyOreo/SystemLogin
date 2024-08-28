import tkinter as tk
from tkinter import messagebox
import getpass

class Usuario:
    def __init__(self, nome="", senha="", email=""):
        self.nome = nome
        self.senha = senha
        self.email = email

def submit_form():
    nome = entry_nome.get()
    senha = entry_senha.get()
    email = entry_email.get()
    
    if "@" not in email:
        messagebox.showerror("Erro", "O e-mail deve conter '@'.")
        return
    
    usuario1 = Usuario(nome, senha, email)
    messagebox.showinfo("Informações do Usuário", f"Nickname: {usuario1.nome}\nSenha: {'*' * len(usuario1.senha)}\nE-mail: {usuario1.email}")


root = tk.Tk()
root.title("Sistema de Login")

#Layout dos widgets
tk.Label(root, text="Nome de usuário:").pack()
entry_nome = tk.Entry(root)
entry_nome.pack()

tk.Label(root, text="Senha:").pack()
entry_senha = tk.Entry(root, show="*")
entry_senha.pack()

tk.Label(root, text="E-mail:").pack()
entry_email = tk.Entry(root)
entry_email.pack()

tk.Button(root, text="Submit", command=submit_form).pack()

#Iniciar o loop principal da interface gráfica
root.mainloop()
