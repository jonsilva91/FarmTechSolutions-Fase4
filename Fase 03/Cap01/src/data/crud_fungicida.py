from datetime import datetime

def inserir_fungicida(cursor, cd_area, quantidade_total):
    """
    Registra uma aplicação de fungicida na tabela Aplicacao.

    Args:
        cursor: Cursor Oracle.
        cd_area: Código da área de plantio.
        quantidade_total: Quantidade total (em L) de fungicida aplicado.
    """
    sql = """
        INSERT INTO Aplicacao (
            cd_aplicacao, dt_aplicacao, tp_aplicacao, vl_quantidade, cd_area
        ) VALUES (
            (SELECT NVL(MAX(cd_aplicacao), 0) + 1 FROM Aplicacao),
            TO_DATE(:1, 'YYYY-MM-DD HH24:MI:SS'),
            'fungicida', :2, :3
        )
    """
    data_aplicacao = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute(sql, (data_aplicacao, quantidade_total, cd_area))


def listar_fungicidas(cursor):
    """
    Lista todas as aplicações de fungicida.
    """
    cursor.execute("""
        SELECT cd_aplicacao, dt_aplicacao, vl_quantidade, cd_area
        FROM Aplicacao
        WHERE tp_aplicacao = 'fungicida'
        ORDER BY dt_aplicacao DESC
    """)
    return cursor.fetchall()


def atualizar_fungicida(cursor, cd_aplicacao, nova_quantidade):
    """
    Atualiza a quantidade aplicada de um fungicida específico.
    """
    sql = """
        UPDATE Aplicacao
        SET vl_quantidade = :1
        WHERE cd_aplicacao = :2 AND tp_aplicacao = 'fungicida'
    """
    cursor.execute(sql, (nova_quantidade, cd_aplicacao))


def deletar_fungicida(cursor, cd_aplicacao):
    """
    Remove um registro de aplicação de fungicida da tabela Aplicacao.
    """
    sql = """
        DELETE FROM Aplicacao
        WHERE cd_aplicacao = :1 AND tp_aplicacao = 'fungicida'
    """
    cursor.execute(sql, (cd_aplicacao,))
