from dados import *

from dados import entrada_dados, listar_dados, atualizar_dados, deletar_dados

def menu():
    while True:
        print("\n=== Sistema de Monitoramento Agrícola ===\n")
        print("1. Inserir nova cultura")
        print("2. Listar culturas")
        print("3. Atualizar área")
        print("4. Deletar cultura")
        print("5. Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            entrada_dados()
        elif opcao == "2":
            listar_dados()
        elif opcao == "3":
            atualizar_dados()
        elif opcao == "4":
            deletar_dados()
        elif opcao == "5":
            print("Finalizando sistema. Até logo!")
            break
        else:
            print("\nOpção inválida. Escolha um número entre 1 e 5.\n")
