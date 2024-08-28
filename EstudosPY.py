print("Bem vindo ao nosso sistema de login")

def object_email():
    while True:
        email = input("Digite seu e-mail: ")
        if "@" in email:
            return email
        else:
            print("O e-mail deve conter '@'. Por favor, tente novamente.")


class usuario:
    def __init__(self, nome="", senha="", email=""):
        self.nome=nome
        self.senha= senha
        self.email= email

usuario1=usuario()

usuario1.nome=input("Digite o nome de usuario que deseja usar \n")
usuario1.senha=input("Digite sua senha \n")
usuario1.email=object_email()

print(f"Nickname:"+usuario1.nome+"\n")
print(f"Senha:"+ usuario1.senha +"\n")
print(f"E-mail"+usuario1.email+"\n")