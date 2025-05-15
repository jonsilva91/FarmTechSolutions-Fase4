from conexao import OracleDB
from data.crud_cultura import *
from data.crud_adubacao import *
from data.crud_fungicida import *
from data.crud_leitura import *
from data.crud_area_plantio import *
from calculos import *
from validacao_dados import *
import traceback
from datetime import datetime



def entrada_dados():
    db = OracleDB()
    cursor = db.cursor

    try:
        print("\nEntrada de Dados:\n")
        tipo_cultura = entrada_opcao("Digite a cultura (Soja ou Milho): ", ["soja", "milho"])
        area_ha = calcular_area()

        germinacao = entrada_float("Poder germinativo das sementes (%): ")
        peso_mil_graos = entrada_float("Peso por mil grãos (g): ")

        produtividade_op = entrada_yn("Calcular produtividade esperada? Y/N: ").strip().lower()
        if produtividade_op == 'y':
            if tipo_cultura == 'soja':
                qtd_vagens = entrada_float("Quantas vagens em 10 plantas? ")
                qtd_graos = entrada_float("Quantos grãos nas vagens? ")
                produtividade_calc = calcular_produtividade(tipo_cultura, qtd_vagens, qtd_graos, germinacao, peso_mil_graos)
            else:
                peso_graos = entrada_float("Peso médio dos grãos coletados (g): ")
                produtividade_calc = calcular_produtividade(tipo_cultura, peso_graos=peso_graos)
        else:
            produtividade_calc = None

        espacamento = 0.4 if tipo_cultura == 'soja' else 0.5
        densidade = calculo_densidade(tipo_cultura, espacamento)
        taxa = calcular_semeadura(densidade, germinacao)
        peso_ha = calcular_peso_area(tipo_cultura, peso_mil_graos, germinacao)

        cursor.execute("SELECT NVL(MAX(cd_cultura), 0) + 1 FROM Cultura")
        cd_cultura = cursor.fetchone()[0]

        cultura = {
            "cd_cultura": cd_cultura,
            "nm_cultura": tipo_cultura,
            "tp_cultura": tipo_cultura
        }

        inserir_cultura(cursor, cultura)

        cursor.execute("SELECT NVL(MAX(cd_area), 0) + 1 FROM Area_Plantio")
        cd_area = cursor.fetchone()[0]

        area = {
            "cd_area": cd_area,
            "vl_area_ha": area_ha,
            "vl_espacamento": espacamento,
            "vl_densidade": densidade,
            "vl_taxa_semeadura": taxa,
            "vl_peso_ha": peso_ha,
            "cd_cultura": cd_cultura,
            "cd_responsavel": 1,
            "ds_produtividade": str(produtividade_calc) if produtividade_calc else None
        }

        inserir_area_plantio(cursor, area)

        
                # 🔸 Adubação
        if entrada_yn("Deseja registrar adubação? (Y/N): ") == 'y':
            if tipo_cultura == 'soja':
                p = entrada_float("P (fósforo) resina (mg/dm³): ")
                k = entrada_float("K (potássio) trocável (cmol/dm³): ")
                prod_est = entrada_float("Estimativa de produção (ton/ha): ")
                p2o5, k2o = calcular_adubo_soja(prod_est, p, k)
                total_adubo = p2o5 + k2o
            else:
                prod_est = entrada_float_intervalo("Estimativa de produção (ton/ha): ", 5, 15)
                destino = entrada_opcao("Finalidade do milho (grao ou silagem): ", ["grao", "silagem"])
                n, p, k = calcular_adubo_milho(prod_est, destino)
                total_adubo = n + p + k

            inserir_adubacao(cursor, cd_area, total_adubo)


        # 🔸 Fungicida
        if entrada_yn("Deseja registrar aplicação de fungicida? (Y/N): ") == 'y':
            nome = input("Nome do produto: ")
            velocidade = entrada_float("Velocidade do trator (m/min): ")
            tanque = entrada_float("Capacidade do tanque (L): ")
            vazao = entrada_float("Vazão do pulverizador (L/min): ")
            num_pulverizadores = entrada_float("Qtd de bicos/pulverizadores: ")
            espacadores = entrada_float("Espaçamento entre bicos (cm): ")
            qtd_lha = entrada_float("Recomendação do fabricante (L/ha): ")

            dosagem, taxa_aplic = calcular_pulverizadores(
                tanque, qtd_lha, vazao, velocidade, num_pulverizadores, espacadores
            )
            fungicida_ha, total_fungicida = calcular_volume_fungicida(
                    area_ha, tanque, dosagem, taxa_aplic
            )

    # Usa a função do CRUD para inserir
            inserir_fungicida(cursor, cd_area, total_fungicida)
                       


        db.conn.commit()
        print("✅ Todos os dados foram salvos com sucesso!\n")

    except Exception as e:
        print("❌ Ocorreu um erro durante a operação:")
        traceback.print_exc()
        db.conn.rollback()

    finally:
        db.fechar()


def listar_dados():
    db = OracleDB()
    cursor = db.cursor
    dados = listar_culturas_com_area(cursor)

    if not dados:
        print("Nenhuma cultura cadastrada.")
        db.fechar()
        return

    print("\nCulturas cadastradas:\n")
    for i, d in enumerate(dados):
        print(f"[{i}] Cultura: {d[1].capitalize()}, Área: {d[3]} ha")

    indice = entrada_opcao("\nSelecione o índice para visualizar os detalhes: ", [str(i) for i in range(len(dados))])
    d = dados[int(indice)]

    print(f"\n--- Detalhes da Cultura '{d[1].capitalize()}' ---")
    print(f"Tipo de Cultura: {d[2]}")
    print(f"Área Total: {d[3]} ha")
    print(f"Espaçamento: {d[4]*100:.1f} cm")
    print(f"Densidade: {d[5]:.2f} sementes por metro")
    print(f"Taxa de Semeadura: {d[6]:.2f} sementes por metro")
    print(f"Peso por Hectare: {d[7]/1000:.2f} Kg/ha")
    print(f"Produtividade Estimada: {str(d[8]) + ' sc/ha' if d[8] is not None else 'Não informada'}\n")

    print("🔹 Aplicações registradas:")
    adubacoes = listar_adubacoes(cursor)
    for a in adubacoes:
        if a[3] == d[9]:
            print(f"  [Adubação] Data: {a[1]}, Quantidade: {a[2]} kg")

    fungicidas = listar_fungicidas(cursor)
    for f in fungicidas:
        if f[3] == d[9]:
            print(f"  [Fungicida] Data: {f[1]}, Quantidade: {f[2]} L")

    db.fechar()



def atualizar_dados():
    db = OracleDB()
    cursor = db.cursor
    dados = listar_culturas_com_area(cursor)

    if not dados:
        print("Nenhuma cultura cadastrada.")
        db.fechar()
        return

    print("\nCulturas cadastradas:\n")
    for i, d in enumerate(dados):
        print(f"[{i}] Cultura: {d[1].capitalize()}, Área: {d[3]} ha")

    indice = entrada_opcao("Selecione o índice da cultura para atualizar: ", [str(i) for i in range(len(dados))])
    d = dados[int(indice)]
    cd_cultura = d[0]
    cd_area = d[9]

    if entrada_yn("Deseja recalcular a área? (Y/N): ") == 'y':
        nova_area = calcular_area()
    else:
        nova_area = d[3]

    germinacao = entrada_float("Novo poder germinativo das sementes (%): ")
    peso_mil_graos = entrada_float("Novo peso por mil grãos (g): ")

    if entrada_yn("Calcular nova produtividade? (Y/N): ") == 'y':
        if d[2] == 'soja':
            qtd_vagens = entrada_float("Quantas vagens em 10 plantas? ")
            qtd_graos = entrada_float("Quantos grãos nas vagens? ")
            produtividade = calcular_produtividade(d[2], qtd_vagens, qtd_graos, germinacao, peso_mil_graos)
        else:
            peso_graos = entrada_float("Peso médio dos grãos coletados (g): ")
            produtividade = calcular_produtividade(d[2], peso_graos=peso_graos)
    else:
        produtividade = d[8]

    espacamento = 0.4 if d[2] == 'soja' else 0.5
    densidade = calculo_densidade(d[2], espacamento)
    taxa = calcular_semeadura(densidade, germinacao)
    peso_ha = calcular_peso_area(d[2], peso_mil_graos, germinacao)

    cursor.execute("""
        UPDATE Area_Plantio SET
            vl_area_ha = :1, vl_espacamento = :2, vl_densidade = :3,
            vl_taxa_semeadura = :4, vl_peso_ha = :5, ds_produtividade = :6
        WHERE cd_cultura = :7
    """, (nova_area, espacamento, densidade, taxa, peso_ha, str(produtividade), cd_cultura))

    # Atualizar adubação
    if entrada_yn("Deseja atualizar a adubação? (Y/N): ") == 'y':
        nova_qtd = entrada_float("Nova quantidade total de adubo (kg): ")
        adubacoes = listar_adubacoes(cursor)
        for a in adubacoes:
            if a[3] == cd_area:
                atualizar_adubacao(cursor, a[0], nova_qtd)
                break

    # Atualizar fungicida
    if entrada_yn("Deseja atualizar a aplicação de fungicida? (Y/N): ") == 'y':
        nova_qtd = entrada_float("Nova quantidade total de fungicida (L): ")
        fungicidas = listar_fungicidas(cursor)
        for f in fungicidas:
            if f[3] == cd_area:
                atualizar_fungicida(cursor, f[0], nova_qtd)
                break

    db.conn.commit()
    print("✅ Atualização concluída com sucesso.")
    db.fechar()




def deletar_dados():
    db = OracleDB()
    cursor = db.cursor
    dados = listar_culturas_com_area(cursor)

    if not dados:
        print("Nenhuma cultura cadastrada.")
        db.fechar()
        return

    print("\nCulturas cadastradas:\n")
    for i, d in enumerate(dados):
        print(f"[{i}] Cultura: {d[1].capitalize()}, Área: {d[3]} ha")

    indice = entrada_opcao("Selecione o índice da cultura a deletar: ", [str(i) for i in range(len(dados))])
    d = dados[int(indice)]
    cd_cultura = d[0]
    cd_area = d[9]

    if entrada_yn(f"Tem certeza que deseja deletar '{d[1].capitalize()}'? (Y/N): ") == 'y':
        adubacoes = listar_adubacoes(cursor)
        for a in adubacoes:
            if a[3] == cd_area:
                deletar_adubacao(cursor, a[0])

        fungicidas = listar_fungicidas(cursor)
        for f in fungicidas:
            if f[3] == cd_area:
                deletar_fungicida(cursor, f[0])

        cursor.execute("DELETE FROM Area_Plantio WHERE cd_cultura = :1", (cd_cultura,))
        cursor.execute("DELETE FROM Cultura WHERE cd_cultura = :1", (cd_cultura,))
        db.conn.commit()
        print("❌ Cultura e todas as aplicações associadas foram removidas.")
    else:
        print("Operação cancelada.")

    db.fechar()


