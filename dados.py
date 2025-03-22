import math
import json
from calculos import *
from validacao_dados import *




def salvar_dados():
    with open("./data/dados.json", "w") as f:
        json.dump(dados, f, indent=4)

def carregar_dados():
    global dados
    try:
        with open("./data/dados.json", "r") as f:
            dados = json.load(f)
    except FileNotFoundError:
        dados = []  
        
        
carregar_dados()


            
def entrada_dados():
    """Função para entrada de dados do usuário"""
    print("\nEntrada de Dados:\n")
    tipo_cultura = entrada_opcao("Digite a cultura (Soja ou Milho): ", ["soja", "milho"])
    area = calcular_area()
    # Dicionário para armazenar insumos
    insumos = {}

    # Adubação (NPK) - Opcional
    adubacao = entrada_yn("Deseja adicionar adubação? (Y/N): ").strip().lower()
    if tipo_cultura == 'soja':
        if adubacao == 'y':
            p_resina = entrada_float("Informe o valor de P(fósforo) resina medido no seu solo(mg/dm³): ")
            k_trocavel = entrada_float("Informe o valor de K(potássio) trocável medido do seu solo (cmol/dm³): ")
            produtividade_adubacao = entrada_float("Informe a estimativa de produção(toneladas/ha): ")
            p2o5_total, k2o_total = calcular_adubo_soja(produtividade_adubacao, p_resina, k_trocavel)  # Chamada da função definida pelo usuário
        
            insumos["adubacao"] = {
                "tipo": "NPK (Nitrogênio, Fósforo, Potássio) sendo que o Nitrôgenio é obtido da própria planta",
                "p_resina": p_resina,
                "k_trocavel": k_trocavel,
                "estimativa_producao": produtividade_adubacao,
                "p2o5_total": p2o5_total,
                "k2o_total": k2o_total
             }
    else:
            if adubacao == 'y':
                produtividade_adubacao = entrada_float_intervalo("Informe a estimativa de produção (toneladas/ha): ", 5, 15)
                tipo_milho = entrada_opcao("Informe a finalidade da plantação do milho (grão ou silagem): ", ["grao", "silagem"])
                n, p2o5, k2o = calcular_adubo_milho(produtividade_adubacao, tipo_milho)
        
                insumos["adubacao"] = {
                    "tipo": "NPK (Nitrogênio, Fósforo, Potássio)",
                    "nitrogênio": n,
                    "fósforo": p2o5,
                    "potássio": k2o,
                    "estimativa_producao": produtividade_adubacao,
                   
                    }
    # Fungicida 
    print('\n Cálculo do Insumo a ser aplicado\n')
    nome_produto = input("Qual o produto que será aplicado? ")
    velocidade = entrada_float("Qual a velocidade média percorrida pelo pulverizador (m/min)? ")
    tanque = entrada_float("Qual o tamanho do tanque do pulverizador (L)? ")
    vazao_pulverizador = entrada_float("Qual a vazão do seu pulverizador do fabricante para aplicação do produto (L/min)? ") #vazão padrão de uma pulverizadora comercial pode virar input no futuro L/min
    num_pulverizadores = entrada_float("Quantos pulverizadores há no seu trator? ")
    espacadores = entrada_float("Qual é o espaçamento entre os pulverizadores em cm? ")
    qtd_recomendado = entrada_float("Qual a recomendação do fabricante para aplicação do produto (L/ha)? ")
    dosagem,taxa_aplicacao = calcular_pulverizadores(tanque,qtd_recomendado, vazao_pulverizador,velocidade,num_pulverizadores,espacadores)  # Chamada para função específica
    fungicida_ha, total_fungicida = calcular_volume_fungicida(area,tanque,dosagem,taxa_aplicacao)
    
    insumos["fungicida"] = {
        "nome": nome_produto,
        "dosagem": dosagem,
        "num_pulverizadores": num_pulverizadores,
        "fungicida_ha": fungicida_ha,
        "total_fungicida": total_fungicida
    }
    
    germinacao = entrada_float("Insira o poder germinativo das sementes indicado no rótulo (%): ")
    peso_mil_graos = entrada_float("Insira o peso por mil grãos do seu híbrido (g): ")
    produtividade = entrada_yn("Gostaria de calcular a produtividade esperada? Y/N ").strip().lower()
    if produtividade == 'y':
        if tipo_cultura =='soja':
            qtd_vagens = entrada_float("Insira quantas vagens foram coletadas em 10 plantas: ")
            qtd_graos_vagens = entrada_float("Quantos grãos no total há nessas vagens: ")
            produtividade = calcular_produtividade(tipo_cultura=tipo_cultura,qtd_vagens=qtd_vagens,qtd_graos_vagens=qtd_graos_vagens,germinacao=germinacao,peso_mil_graos=peso_mil_graos)
        else:
            peso_graos = entrada_float("Insira o peso médio dos grãos coletados (g): ")
            produtividade = calcular_produtividade(tipo_cultura=tipo_cultura,peso_graos=peso_graos)
    else:
        produtividade = 'Não foi previsto produtividade para essa cultura'
    
    #espacaçamento entre linhas e plantas 
    
    if tipo_cultura == 'soja':
        espacamento = 0.4 #espaçamento de 40cm padrão para soja segundo embrapa 
    else: 
        espacamento = 0.5 #espaçamento de 50cm padrão para milho  segundo embrapa 
    densidade = calculo_densidade(tipo_cultura,espacamento)
    taxa_semeadura = calcular_semeadura(densidade, germinacao)
    peso_por_hectare = calcular_peso_area(tipo_cultura,peso_mil_graos,germinacao)
    
    
    entrada = {"cultura": tipo_cultura,"area": area,
        "densidade": densidade,
        "espacamento": espacamento,
        "taxa_semeadura": taxa_semeadura,
        "peso_por_hectare": peso_por_hectare,
        "produtividade": produtividade,
        "insumos": insumos  
    }
    dados.append(entrada)
    salvar_dados()
    print("Cultura adicionada com sucesso!\n")

def saida_dados():
    carregar_dados()
    if not dados:
        print("Nenhum dado cadastrado!\n")
        return
    
    for i, d in enumerate(dados):
        print(f"\n[{i}] Cultura: {d['cultura'].capitalize()}, Área: {d['area']:.2f} hectares\n")
        print(f"   - Espaçamento: {d['espacamento']*100} cm entre plantas e linhas")
        print(f"   - Densidade: Sua densidade é {d['densidade']:.2f} sementes por metro linear")
        print(f"   - Taxa de Semeadura: Deverá ajustar para {d['taxa_semeadura']:.2f} sementes por metro")
        print(f"   - Peso por Hectare: Serão usados {d['peso_por_hectare']/1000:.2f} Kg de sementes por hectare")
        print(f"   - Produtividade: {d['produtividade']} em sacas/hectare")

                # Exibir insumos
        if d["insumos"]:
            print("\n   --- Insumos, Cálculos de Manejo ---\n")
            for nome_insumo, detalhes in d["insumos"].items():
                if nome_insumo.lower() == "fungicida":
                    print(f"   {nome_insumo.capitalize()}: Cálculos para aplicação\n")
                else:
                    print(f"   {nome_insumo.capitalize()}:\n")

                for chave, valor in detalhes.items():
                    if chave == "estimativa_producao":
                        print(f"      {chave.capitalize()}: {valor:.2f} t/ha\n")
                    elif chave == "nome":
                        print(f" \nCálculo de aplicação de {valor}: \n")
                    elif chave == "dosagem":
                        print(f"      {chave.capitalize()}: {valor:.2f} L de produto por tanque")
                    elif chave == "fungicida_ha":
                        print(f"      {chave.capitalize()}: Cada tanque de produto cobrirá {valor:.2f} hectares")
                    elif chave == "total_fungicida":
                        print(f"      {chave.capitalize()}: Utilizar no total {valor:.2f} litros de produto em toda lavoura")
                    elif chave == "p2o5_total" or chave == "k2o_total":
                        print(f"      {chave.capitalize()}: Usar {valor:.2f} Kg/ha sendo no total para sua lavoura {valor*d['area']:.2f} Kg\n")
                    elif chave == "nitrogênio" or chave == "fósforo" or  chave == "potássio":
                        print(f"      {chave.capitalize()}: Usar {valor:.2f} Kg/ha sendo no total para sua lavoura {valor*d['area']:.2f} Kg\n")
                    else:
                        print(f"      {chave}: {valor:.2f}" if isinstance(valor, float) else f"      {chave}: {valor}")

    print()

def atualizar_dados():
    carregar_dados()
    if not dados:
        print("\nNão há dados para atualizar.\n")
        return

    print("\nSelecione a cultura para atualizar:")
    for i, d in enumerate(dados):
        print(f"[{i}] Cultura: {d['cultura']}, Área: {d['area']:.2f} hectares")
    
    try:
        indice = int(input("Digite o índice do dado a ser atualizado: "))
        if 0 <= indice < len(dados):
            cultura = dados[indice]['cultura']
            print(f"\nAtualizando dados para a cultura: {cultura}")

            # Atualizar área
            nova_area = entrada_yn("Gostaria de recalcular a área? (Y/N) ").strip().lower()
            if nova_area == 'y':
                area = calcular_area()  
            else:
                area = dados[indice]['area']

            # Atualizar adubação se existir
            if "adubacao" in dados[indice]["insumos"] and "p_resina" in dados[indice]["insumos"]["adubacao"]:

                print("\n-- Atualização da Adubação --")
                p_resina = entrada_float_opcional(f"Novo P resina (mg/dm³) (Atual: {dados[indice]['insumos']['adubacao']['p_resina']}): ",dados[indice]['insumos']['adubacao']['p_resina'])

                k_trocavel = entrada_float_opcional(f"Novo K trocável (cmol/dm³) (Atual: {dados[indice]['insumos']['adubacao']['k_trocavel']}): ",dados[indice]['insumos']['adubacao']['k_trocavel'])

                estimativa_producao = entrada_float_opcional(f"Nova estimativa de produção (t/ha) (Atual: {dados[indice]['insumos']['adubacao']['estimativa_producao']}): ",dados[indice]['insumos']['adubacao']['estimativa_producao'])

                # Recalcular adubação com os novos valores
                p2o5_total, k2o_total = calcular_adubo_soja(estimativa_producao, p_resina, k_trocavel)

                dados[indice]['insumos']['adubacao'].update({
                    "p_resina": p_resina,
                    "k_trocavel": k_trocavel,
                    "estimativa_producao": estimativa_producao,
                    "p2o5_total": p2o5_total,
                    "k2o_total": k2o_total
                })
            elif "adubacao" in dados[indice]["insumos"] and "nitrogênio" in dados[indice]["insumos"]["adubacao"]:
            
                print("\n-- Atualização da Adubação --")
                produtividade_adubacao = entrada_float_opcional(f"Nova estimativa de produção (t/ha) (Atual: {dados[indice]['insumos']['adubacao']['estimativa_producao']}): ",dados[indice]['insumos']['adubacao']['estimativa_producao'])
                tipo_milho = entrada_opcao("Informe a finalidade da plantação do milho (grão ou silagem): ", ["grao", "silagem"])

                # Recalcular adubação do milho com os novos valores
                n, p2o5, k2o = calcular_adubo_milho(produtividade_adubacao, tipo_milho)

                dados[indice]['insumos']['adubacao'].update({
                    "nitrogênio": n,
                    "fósforo": p2o5,
                    "potássio": k2o,
                    "estimativa_producao": produtividade_adubacao,
                })
            # Atualizar fungicida 
            if "fungicida" in dados[indice]['insumos']:
                print("\n-- Atualização do Fungicida --\n")
                nome_produto = input("Qual o produto que será aplicado? ")
                velocidade = entrada_float("Qual a velocidade média percorrida pelo pulverizador (m/min)? ")
                tanque = entrada_float("Qual o tamanho do tanque do pulverizador (L)? ")
                vazao_pulverizador = entrada_float("Qual a vazão do seu pulverizador do fabricante para aplicação do produto (L/min)? ") #vazão padrão de uma pulverizadora comercial pode virar input no futuro L/min
                num_pulverizadores = entrada_float_opcional(f"Novo número de pulverizadores (Atual: {dados[indice]['insumos']['fungicida']['num_pulverizadores']}): ",dados[indice]['insumos']['fungicida']['num_pulverizadores'])
                espacadores = entrada_float("Qual é o espaçamento entre os pulverizadores em cm? ")
                qtd_recomendado = entrada_float("Qual a recomendação do fabricante para aplicação do produto (L/ha)? ")
                               

                # Recalcular volume e total de fungicida com os novos valores
                
                dosagem,taxa_aplicacao = calcular_pulverizadores(tanque,qtd_recomendado, vazao_pulverizador,velocidade,num_pulverizadores,espacadores)  
                fungicida_ha, total_fungicida = calcular_volume_fungicida(area,tanque,dosagem,taxa_aplicacao)

                dados[indice]['insumos']['fungicida'].update({
                    "nome": nome_produto,
                    "dosagem": dosagem,
                    "num_pulverizadores": num_pulverizadores,
                    "fungicida_ha": fungicida_ha,
                    "total_fungicida": total_fungicida
                })

            # Atualizar dados gerais
            germinacao = entrada_float(f"Novo poder germinativo das sementes (%):")
            peso_mil_graos = entrada_float(f"Novo peso por mil grãos (g):")
            

            produtividade_opcao = entrada_yn("Gostaria de recalcular a produtividade esperada? (Y/N) ").strip().lower()
            if produtividade_opcao == 'y':
                if cultura =='soja':
                    qtd_vagens = float(input("Insira quantas vagens foram coletadas em 10 plantas: "))
                    qtd_graos_vagens = float(input("Quantos grãos no total há nessas vagens: "))
                    produtividade = calcular_produtividade(tipo_cultura=cultura,qtd_vagens=qtd_vagens,qtd_graos_vagens=qtd_graos_vagens,germinacao=germinacao,peso_mil_graos=peso_mil_graos)
                else:
                    peso_graos = float(input("Insira o peso médio dos grãos coletados (g): "))
                    produtividade = calcular_produtividade(tipo_cultura=cultura,peso_graos=peso_graos)
                    
            else:
                produtividade = dados[indice]['produtividade']
                
            #setar espaçamento
            if cultura =='soja':
                densidade = calculo_densidade(cultura, espacamento=0.4)
            else:
                densidade = calculo_densidade(cultura, espacamento=0.5)

            taxa_semeadura = calcular_semeadura(densidade, germinacao)
            peso_por_hectare = calcular_peso_area(cultura, peso_mil_graos, germinacao)

            dados[indice].update({
                "area": area,
                "densidade": densidade,
                "taxa_semeadura": taxa_semeadura,
                "peso_por_hectare": peso_por_hectare,
                "produtividade": produtividade,
            })

            salvar_dados()
            print("\nDado atualizado com sucesso!\n")
        else:
            print("\nÍndice inválido!\n")
    except ValueError:
        print("\nEntrada inválida! Digite um número.\n")


def deletar_dados():
    carregar_dados()
    if not dados:
        print("\nNenhum dado para remover.\n")
        return

    print("\nDados cadastrados:\n")
    for i, d in enumerate(dados):
        print(f"[{i}] Cultura: {d['cultura']}, Área: {d['area']:.2f} hectares")

    entrada = entrada_opcao("\nDigite o índice do dado a ser removido (ou 'V' para voltar): ", 
                            [str(i) for i in range(len(dados))] + ['v'])

    if entrada == 'v':
        print("\nOperação cancelada. Nenhum dado foi removido.\n")
        return

    indice = int(entrada)
    confirmacao = entrada_yn(f"\nTem certeza que deseja remover '{dados[indice]['cultura']}'? (Y/N): ")

    if confirmacao == 'y':
        removido = dados.pop(indice)
        salvar_dados()
        print(f"\nDado removido com sucesso! Cultura: {removido['cultura']}, Área: {removido['area']:.2f} hectares\n")
    else:
        print("\nRemoção cancelada.\n")