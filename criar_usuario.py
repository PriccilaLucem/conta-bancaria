from classes.usuario import Usuario

def criar_usuario():
    nome = input("Digite seu nome ")
    cpf = input("Digite seu cpf ")
    conta_bancaria = input("Digite sua conta bancaria ")
    return Usuario(nome, cpf, conta_bancaria)

        
