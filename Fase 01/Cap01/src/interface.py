from dados import *

def menu():
    """Função que exibe o menu"""
    while True:
        print("\nMenu:")
        print("1. Entrada de dados")
        print("2. Saída de dados")
        print("3. Atualizar dados")
        print("4. Deletar dados")
        print("5. Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == '1':
            try:
                entrada_dados()
            except Exception as e:
                print(f"Erro ao inserir dados: {e}")
        elif opcao == '2':
            try:
                saida_dados()
            except Exception as e:
                print(f"Erro ao exibir dados: {e}")
        elif opcao == '3':
            try:
                atualizar_dados()
            except Exception as e:
                print(f"Erro ao atualizar dados: {e}")
        elif opcao == '4':
            try:
                deletar_dados()
            except Exception as e:
                print(f"Erro ao deletar dados: {e}")
        elif opcao == '5':
            print("\nSaindo do programa...\n")
            break
        else:
            print("\nOpção inválida. Escolha um número entre 1 e 5.\n")
