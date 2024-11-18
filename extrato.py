import globais

def exibir_extrato():
    output = "\n================ EXTRATO ================\n"
    if not globais.extrato:
        output += "Não foram realizadas movimentações.\n"
    else:
        output += globais.extrato + "\n"
    output += f"\nSaldo: R$ {globais.saldo:.2f}\n"
    output += "=========================================="
    return output
