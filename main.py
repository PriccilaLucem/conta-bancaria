from abc import ABC, abstractmethod
from datetime import date


# Classe Histórico
class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)


# Interface Transacao
class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta):
        pass


# Classe Deposito
class Deposito(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        conta.saldo += self.valor
        conta.historico.adicionar_transacao(f"Depósito de R$ {self.valor:.2f}")


# Classe Saque
class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        if conta.saldo >= self.valor:
            conta.saldo -= self.valor
            conta.historico.adicionar_transacao(f"Saque de R$ {self.valor:.2f}")
        else:
            print("Saldo insuficiente.")


# Classe Cliente
class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)


# Classe PessoaFisica (herança de Cliente)
class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_nascimento, endereco):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento


# Classe Conta
class Conta:
    def __init__(self, cliente, numero, agencia):
        self.saldo = 0.0
        self.numero = numero
        self.agencia = agencia
        self.cliente = cliente
        self.historico = Historico()

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.historico.adicionar_transacao(f"Saque de R$ {valor:.2f}")
            return True
        else:
            print("Saldo insuficiente.")
            return False

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.historico.adicionar_transacao(f"Depósito de R$ {valor:.2f}")
            return True
        else:
            print("Valor inválido.")
            return False


# Classe ContaCorrente (herança de Conta)
class ContaCorrente(Conta):
    def __init__(self, cliente, numero, agencia, limite, limite_saques):
        super().__init__(cliente, numero, agencia)
        self.limite = limite
        self.limite_saques = limite_saques
