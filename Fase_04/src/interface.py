from dados import entrada_dados, listar_dados, atualizar_dados, deletar_dados
from clima_api import obter_dados_climaticos  # ajuste o caminho se necessário

def menu():
    while True:
        print("\n=== Sistema de Monitoramento Agrícola ===\n")
        print("1. Inserir nova cultura")
        print("2. Listar culturas")
        print("3. Atualizar área")
        print("4. Deletar cultura")
        print("5. Mostrar clima atual")
        print("6. Sair")

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
            try:
                temp, umid, chuva, cond = obter_dados_climaticos()
                print("\n🌤️  Clima Atual:")
                print(f"  • Temperatura: {temp:.1f}°C")
                print(f"  • Umidade: {umid:.0f}%")
                print(f"  • Precipitação (última hora): {chuva} mm")
                print(f"  • Condição: {cond.capitalize()}\n")
            except Exception as e:
                print("❌ Erro ao obter dados climáticos:")
                import traceback; traceback.print_exc()
        elif opcao == "6":
            print("Finalizando sistema. Até logo!")
            break
        else:
            print("\nOpção inválida. Escolha um número entre 1 e 6.\n")
