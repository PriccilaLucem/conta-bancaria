from depositar import depositar
from sacar import sacar
from extrato import exibir_extrato
from criar_usuario import criar_usuario
def main():
    while True:
        print("""
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
[c] Conta
        """)
        opcao = input("=> ").lower()

        match opcao:
            case "u":
                criar_usuario()
            case "d":
                depositar()
            case "s":
                sacar()
            case "e":
                extrato = exibir_extrato()
                print(extrato)
            case "q":
                print("Obrigado por usar nosso sistema bancário. Até mais!")
                break
            case _:
                print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()
