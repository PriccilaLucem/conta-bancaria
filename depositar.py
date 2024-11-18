import globais

def depositar():
    valor = float(input("Informe o valor do depósito: "))
    if valor > 0:
        globais.saldo += valor
        globais.extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")
