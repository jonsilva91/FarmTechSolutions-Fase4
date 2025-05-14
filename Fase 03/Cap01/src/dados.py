from conexao import OracleDB
from data.crud_cultura import inserir_cultura, listar_culturas_com_area, atualizar_area, deletar_cultura
from data.crud_adubacao import inserir_adubacao
from data.crud_fungicida import inserir_fungicida
from data.crud_leitura import inserir_leitura
from data.crud_area_plantio import inserir_area_plantio
from calculos import *
from validacao_dados import *
import traceback


def entrada_dados():
    db = OracleDB()
    cursor = db.cursor

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
    print("Calculando densidade...")
    densidade = calculo_densidade(tipo_cultura, espacamento)
    print("Densidade:", densidade)
    print("Calculando taxa de semeadura...")
    taxa = calcular_semeadura(densidade, germinacao)
    print("Taxa:", taxa)
    print("Calculando peso por hectare...")
    peso_ha = calcular_peso_area(tipo_cultura, peso_mil_graos, germinacao)

    print("Gerando próximo código de cultura...")
    # Gerar próximo código de cultura
    cursor.execute("SELECT NVL(MAX(cd_cultura), 0) + 1 FROM Cultura")
    cd_cultura = cursor.fetchone()[0]
    print("Código da cultura:", cd_cultura)
    cultura = {
        "cd_cultura": cd_cultura,
        "nm_cultura": tipo_cultura,
        "tp_cultura": tipo_cultura  # ou defina por lógica se quiser
    }

    inserir_cultura(cursor, cultura)
    print("Gerando próximo código de area...")

    # Gerar próximo código de área
    cursor.execute("SELECT NVL(MAX(cd_area), 0) + 1 FROM Area_Plantio")
    cd_area = cursor.fetchone()[0]
    print("Código da area:", cd_area)
    area = {
        "cd_area": cd_area,
        "vl_area_ha": area_ha,
        "vl_espacamento": espacamento,
        "vl_densidade": densidade,
        "vl_taxa_semeadura": taxa,
        "vl_peso_ha": peso_ha,
        "cd_cultura": cd_cultura,
        "cd_responsavel": 1,  # por enquanto fixo
        "ds_produtividade": str(produtividade_calc) if produtividade_calc else None
    }

    try:
        print("Inserindo área de plantio no banco...")
        print("Conteúdo do dicionário área:")
        for k, v in area.items():
            print(f"  {k}: {v}")
    
        inserir_area_plantio(cursor, area)
        print("commit:")
        db.conn.commit()
        print("✅ Cultura e área cadastradas com sucesso!\n")

    except Exception as e:
        print("❌ Erro capturado no Oracle:")
        traceback.print_exc()  # Mostra o stack trace completo
        db.conn.rollback()
    finally:
        db.fechar()


def listar_dados():
    db = OracleDB()
    dados = listar_culturas_com_area(db.cursor)

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
    print(f"Produtividade Estimada: {d[8] if d[8] else 'Não informada'}\n")

    db.fechar()


def atualizar_dados():
    db = OracleDB()
    listar_dados()
    cd = int(input("Digite o ID da cultura a atualizar: "))
    nova_area = entrada_float("Nova área: ")
    atualizar_area(db.cursor, cd, nova_area)
    db.conn.commit()
    print("✅ Atualizado!")
    db.fechar()


def deletar_dados():
    db = OracleDB()
    listar_dados()
    cd = int(input("Digite o ID da cultura a deletar: "))
    deletar_cultura(db.cursor, cd)
    db.conn.commit()
    print("❌ Removido!")
    db.fechar()
