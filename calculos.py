import math
from validacao_dados import entrada_opcao

def calcular_area():
    #Solicita dados ao usuário e calcula a área com base na figura geométrica escolhida, retornando em hectares.
    print("\n Escolha a forma do campo para calcular a área:")
    print("1 - Retângulo\n2 - Círculo\n3 - Triângulo\n4 - Trapézio\n5 - Personalizado")
    
    escolha = entrada_opcao("Digite o número da forma geométrica: ", ["1", "2", "3", "4"])

    if escolha == "1":
        base = float(input("Digite a largura/base da área (m): "))
        altura = float(input("Digite o comprimento/altura da área (m): "))
        area = base * altura

    elif escolha == "2":
        raio = float(input("Digite o raio da área circular (m): "))
        area = math.pi * (raio ** 2)

    elif escolha == "3":
        base = float(input("Digite a base do triângulo (m): "))
        altura = float(input("Digite a altura do triângulo (m): "))
        area = (base * altura) / 2

    elif escolha == "4":
        base_maior = float(input("Digite a base maior do trapézio (m): "))
        base_menor = float(input("Digite a base menor do trapézio (m): "))
        altura = float(input("Digite a altura do trapézio (m): "))
        area = ((base_maior + base_menor) * altura) / 2

    elif escolha == "5":
        print("🔹 Para cálculo personalizado, digite a fórmula da área usando 'x' e 'y' como variáveis.")
        formula = input("Exemplo: 'x * y / 2' → ").strip()
        x = float(input("Digite o valor de 'x': "))
        y = float(input("Digite o valor de 'y': "))
        try:
            area = eval(formula, {"x": x, "y": y, "math": math})
        except Exception as e:
            print(f"Erro ao calcular: {e}")
            return None

    else:
        print(" Opção inválida! Tente novamente.")
        return None

    # Conversão para hectares
    area_hectares = area / 10_000

    print(f"\n✅ Área calculada: {area:.2f} m² ({area_hectares:.2f} hectares)\n")
    return area_hectares

#Função para calcular a quantidade de insumo necessária

def calcular_adubo_soja(produtividade, p_resina, k_trocavel):
    """Calcula a quantidade de adubo necessário com base na tabela de adubação."""
    # Tabela de recomendação de P2O5 (kg/ha) com base na produtividade esperada e P-resina (mg/dm³)
    tabela_p2o5 = {
        ("<2.0", (50, 40, 30, 20)),
        ("2.0-2.5", (60, 50, 40, 20)),
        ("2.5-3.0", (80, 60, 40, 20)),
        ("3.0-3.5", (90, 70, 50, 30)),
        (">3.5", (80, 50, 40, 0))
    }
    
    # Tabela de recomendação de K2O (kg/ha) com base no potássio trocável (mmolc/dm³)
    tabela_k2o = {
        ("<2.0", (60, 40, 20, 0)),
        ("2.0-2.5", (70, 50, 30, 20)),
        ("2.5-3.0", (70, 50, 50, 20)),
        ("3.0-3.5", (80, 60, 50, 30)),
        (">3.5", (80, 60, 60, 40))
    }
    
    # Encontrar valores correspondentes na tabela
    def encontrar_valor(tabela, produtividade):
        for chave, valores in tabela:
            if "-" in chave:
                lim_inf, lim_sup = map(float, chave.split("-"))
                if lim_inf <= produtividade <= lim_sup:
                    return valores
            elif "<" in chave and produtividade < float(chave[1:]):
                return valores
            elif ">" in chave and produtividade > float(chave[1:]):
                return valores
        return None
    
    valores_p2o5 = encontrar_valor(tabela_p2o5, produtividade)
    valores_k2o = encontrar_valor(tabela_k2o, produtividade)
    
    if not valores_p2o5 or not valores_k2o:
        print("Erro: Não foi possível encontrar os valores na tabela.")
        return
    
    # Selecionar a quantidade de P2O5 e K2O conforme os níveis de P-resina e K trocável
    if p_resina < 7:
        p2o5_ha = valores_p2o5[0]
    elif 7 <= p_resina < 16:
        p2o5_ha = valores_p2o5[1]
    elif 16 <= p_resina < 40:
        p2o5_ha = valores_p2o5[2]
    else:
        p2o5_ha = valores_p2o5[3]
    
    if k_trocavel < 0.8:
        k2o_ha = valores_k2o[0]
    elif 0.8 <= k_trocavel < 1.5:
        k2o_ha = valores_k2o[1]
    elif 1.5 <= k_trocavel < 3.0:
        k2o_ha = valores_k2o[2]
    else:
        k2o_ha = valores_k2o[3]
    
    # Calcular a quantidade total para a área plantada
    p2o5_total = p2o5_ha 
    k2o_total = k2o_ha 
    
    return p2o5_total, k2o_total


def calcular_adubo_milho(produtividade, tipo):
    """
    Calcula a quantidade de adubo necessária com base na produtividade esperada e no tipo de milho (grão ou silagem).
    
    :param produtividade: Produtividade esperada (ton/ha)
    :param tipo: Tipo de milho ('grao' ou 'silagem')
    :return: Quantidade de N, P2O5 e K2O (kg/ha)
    """
    # Tabelas de adubação com base na produtividade esperada (kg/ha)
    tabela_adubacao = {
        5:  {'grao': (120, 85, 31),  'silagem': (195, 105, 145)},
        6:  {'grao': (144, 102, 37), 'silagem': (234, 126, 174)},
        7:  {'grao': (168, 119, 43), 'silagem': (273, 147, 203)},
        8:  {'grao': (192, 136, 49), 'silagem': (312, 168, 232)},
        9:  {'grao': (216, 153, 55), 'silagem': (351, 189, 261)},
        10: {'grao': (240, 170, 61), 'silagem': (390, 210, 290)},
        11: {'grao': (264, 187, 68), 'silagem': (429, 231, 319)},
        12: {'grao': (288, 204, 74), 'silagem': (468, 252, 348)},
        13: {'grao': (312, 221, 80), 'silagem': (507, 273, 377)},
        14: {'grao': (336, 238, 86), 'silagem': (546, 294, 406)},
        15: {'grao': (360, 255, 92), 'silagem': (585, 315, 435)},
    }
    
    if produtividade not in tabela_adubacao:
        raise ValueError("Produtividade fora da faixa disponível (5-15 ton/ha).")
    if tipo not in ['grao', 'silagem']:
        raise ValueError("Tipo inválido. Use 'grao' ou 'silagem'.")
    
    return tabela_adubacao[produtividade][tipo]
#Função para calcular a densidade de plantas por metro linear

def calculo_densidade(tipo_cultura,espacamento):
  
    if tipo_cultura == 'soja':
       
        densidade = (300000*espacamento)/10000
        
    else:
        densidade = (60000*espacamento)/10000
    return densidade


#Função para calcular a taxa de semeadura

def calcular_semeadura(densidade, germinacao):
    
   
       
    taxa_semeadura = (densidade*100)/(germinacao)
        
    
    return taxa_semeadura
    
#Função para calcular o peso de grãos por hectare

def calcular_peso_area(tipo_cultura,peso_mil_graos,germinacao):
    
    if tipo_cultura == 'soja':
#calculo de quantidade de grão por hectare considerando uma perda de 10% de produção
        qtd_por_hectare = ((300000*100)/(germinacao))*1.1
#calculo de peso de grãos por hectare 
        peso_por_hectare = (qtd_por_hectare*peso_mil_graos)/1000
    else:
#calculo de quantidade de grão por hectare considerando uma perda de 10% de produção
        qtd_por_hectare = ((60000*100)/(germinacao))*1.1
#calculo de peso de grãos por hectare 
        peso_por_hectare = (qtd_por_hectare*peso_mil_graos)/1000
   
    return peso_por_hectare

def calcular_produtividade(tipo_cultura, qtd_vagens=None, qtd_graos_vagens=None, germinacao=None, peso_mil_graos=None, peso_graos=None):
    
    if tipo_cultura == 'soja':
        
        vagens_planta = qtd_vagens/10
        grao_vagem = qtd_graos_vagens/qtd_vagens
        
        produtividade = (((((300000*100)/(germinacao))*1.1)* vagens_planta * grao_vagem*peso_mil_graos)/60000)/1000
    else:
        produtividade = ((peso_graos/1000)*60000)/1000
    return round(produtividade,2)

def calcular_pulverizadores(qtd_recomendado,tanque,vazao_pulverizador, velocidade,num_pulverizadores,espacadores):
    #calculo de área tratada em ha/min
    area_tratada = (velocidade*(num_pulverizadores*(espacadores/100)))/10000
    
    #taxadeaplicacao
    taxa_aplicacao = vazao_pulverizador/area_tratada
    
    #dosagem por pulverizador em l
    dosagem = (tanque*qtd_recomendado)/taxa_aplicacao
    return dosagem,taxa_aplicacao

def calcular_volume_fungicida(area,tanque,dosagem,taxa_aplicacao):
    
    fungicida_ha = tanque/taxa_aplicacao #calculo de quantos hectares um tanque cobre
    total_fungicida = (area/fungicida_ha) * dosagem #calculo de quanto de produto vai precisar 
    
    return fungicida_ha,total_fungicida