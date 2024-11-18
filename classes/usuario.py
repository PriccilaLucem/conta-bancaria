import globais

class Usuario:
    def __init__(self, nome, cpf, conta_bancaria):
        self.nome = nome
        self.cpf = cpf
        self.conta = conta_bancaria

    def __str__(self):
        return f"Usuário: {self.nome} (CPF: {self.cpf})"