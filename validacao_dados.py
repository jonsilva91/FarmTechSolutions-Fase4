def entrada_opcao(mensagem, opcoes_validas):
    """Garante que a entrada seja uma das opções fornecidas."""
    while True:
        valor = input(mensagem).strip().lower()
        if valor in opcoes_validas:
            return valor
        print(f"Entrada inválida! Escolha entre: {', '.join(opcoes_validas)}")

def entrada_float(mensagem):
    """Garante que a entrada seja um número float válido."""
    while True:
        try:
            valor = float(input(mensagem))
            if valor > 0:  # Evita valores negativos se necessário
                return valor
            else:
                print("O valor não pode ser negativo ou zero!")
        except ValueError:
            print("Entrada inválida! Digite um número válido.")

def entrada_float_opcional(mensagem, valor_atual):
    """Permite entrada opcional de número float, mantendo o valor atual se vazio."""
    while True:
        entrada = input(mensagem).strip()
        if entrada == "":
            return valor_atual  # Mantém o valor atual
        try:
            valor = float(entrada)
            if valor > 0:  # Se necessário, evitar números negativos
                return valor
            else:
                print("O valor não pode ser negativo ou zero!")
        except ValueError:
            print("Entrada inválida! Digite um número válido ou pressione Enter para manter o valor atual.")
            
def entrada_float_intervalo(mensagem, minimo, maximo):
    """Garante que a entrada seja um número float dentro de um intervalo específico."""
    while True:
        try:
            valor = float(input(mensagem))
            if minimo <= valor <= maximo:
                return valor
            else:
                print(f"O valor deve estar entre {minimo} e {maximo}!")
        except ValueError:
            print("Entrada inválida! Digite um número válido.")

def entrada_yn(mensagem):
    """Garante que a entrada seja 'y' ou 'n'."""
    while True:
        valor = input(mensagem).strip().lower()
        if valor in ["y", "n"]:
            return valor
        print("Entrada inválida! Digite 'Y' para sim ou 'N' para não.")


