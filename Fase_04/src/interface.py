from dados import entrada_responsavel, entrada_dados, listar_dados, atualizar_dados, deletar_dados
from clima_api import obter_dados_climaticos 


def menu():
    while True:
        print("\n=== Sistema de Monitoramento Agrícola ===\n")
        print("1. Cadastrar responsável")
        print("2. Inserir nova cultura")
        print("3. Listar culturas")
        print("4. Atualizar área")
        print("5. Deletar cultura")
        print("6. Mostrar clima atual")
        print("7. Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            entrada_responsavel()
        elif opcao == "2":
            entrada_dados()
        elif opcao == "3":
            listar_dados()
        elif opcao == "4":
            atualizar_dados()
        elif opcao == "5":
            deletar_dados()
        elif opcao == "6":
            try:
                temp, umid, chuva, cond = obter_dados_climaticos()
                print("\n🌤️  Clima Atual:")
                print(f"  • Temperatura: {temp:.1f}°C")
                print(f"  • Umidade: {umid:.0f}%")
                print(f"  • Precipitação (última hora): {chuva} mm")
                print(f"  • Condição: {cond.capitalize()}\n")
            except Exception:
                print("❌ Erro ao obter dados climáticos")
        elif opcao == "7":
            print("Finalizando sistema. Até logo!")
            break
        else:
            print("\nOpção inválida. Escolha um número entre 1 e 7.\n")


if __name__ == '__main__':
    menu()