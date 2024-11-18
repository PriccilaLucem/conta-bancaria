import globais

def sacar():
    valor = float(input("Informe o valor do saque: "))

    excedeu_saldo = valor > globais.saldo
    excedeu_limite = valor > globais.limite
    excedeu_saques = globais.numero_saques >= globais.LIMITE_SAQUES

    if excedeu_saldo:
        return "Operação falhou! Você não tem saldo suficiente."
    elif excedeu_limite:
        return "Operação falhou! O valor do saque excede o limite."
    elif excedeu_saques:
        return "Operação falhou! Número máximo de saques excedido."
    elif valor > 0:
        globais.saldo -= valor
        globais.extrato += f"Saque: R$ {valor:.2f}\n"
        globais.numero_saques += 1
        return f"Saque de R$ {valor:.2f} realizado com sucesso!"
    else:
        return "Operação falhou! O valor informado é inválido."
