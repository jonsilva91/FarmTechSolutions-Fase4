from conexao import OracleDB
from crud_cultura import inserir_cultura, listar_culturas, atualizar_area, deletar_cultura
from crud_adubacao import inserir_adubacao
from crud_fungicida import inserir_fungicida
from crud_leitura import inserir_leitura
from calculos import *
from validacao_dados import *
from interface import entrada_opcao, entrada_float, entrada_yn


def entrada_dados():
    db = OracleDB()
    cursor = db.cursor

    print("\nEntrada de Dados:\n")
    tipo_cultura = entrada_opcao("Digite a cultura (Soja ou Milho): ", ["soja", "milho"])
    area = calcular_area()

    germinacao = entrada_float("Poder germinativo das sementes (%): ")
    peso_mil_graos = entrada_float("Peso por mil grãos (g): ")

    produtividade = entrada_yn("Calcular produtividade esperada? Y/N: ").strip().lower()
    if produtividade == 'y':
        if tipo_cultura == 'soja':
            qtd_vagens = entrada_float("Quantas vagens em 10 plantas? ")
            qtd_graos = entrada_float("Quantos grãos nas vagens? ")
            produtividade_calc = calcular_produtividade(tipo_cultura, qtd_vagens, qtd_graos, germinacao, peso_mil_graos)
        else:
            peso_graos = entrada_float("Peso médio dos grãos coletados (g): ")
            produtividade_calc = calcular_produtividade(tipo_cultura, peso_graos=peso_graos)
    else:
        produtividade_calc = "Não informado"

    espacamento = 0.4 if tipo_cultura == 'soja' else 0.5
    densidade = calculo_densidade(tipo_cultura, espacamento)
    taxa = calcular_semeadura(densidade, germinacao)
    peso_ha = calcular_peso_area(tipo_cultura, peso_mil_graos, germinacao)

    cultura = {
        "nm_cultura": tipo_cultura,
        "vl_area": area,
        "vl_densidade": densidade,
        "vl_espacamento": espacamento,
        "vl_taxa_semeadura": taxa,
        "vl_peso_hectare": peso_ha,
        "ds_produtividade": str(produtividade_calc)
    }

    inserir_cultura(cursor, cultura)
    db.conn.commit()
    print("✅ Cultura salva com sucesso!")

    db.fechar()


def listar_dados():
    db = OracleDB()
    dados = listar_culturas(db.cursor)
    for row in dados:
        print(f"ID: {row[0]}, Cultura: {row[1]}, Área: {row[2]} ha, Produtividade: {row[7]}")
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
