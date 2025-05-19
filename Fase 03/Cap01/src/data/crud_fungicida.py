from datetime import datetime

def inserir_fungicida(cursor, cd_area, quantidade_total, nome_produto):
    """
    Registra uma aplicação de fungicida na tabela Aplicacao.
    """
    sql = """
        INSERT INTO Aplicacao (
            cd_aplicacao, dt_aplicacao, tp_aplicacao,
            vl_quantidade, nm_produto, cd_area
        ) VALUES (
            (SELECT NVL(MAX(cd_aplicacao), 0) + 1 FROM Aplicacao),
            TO_DATE(:1, 'YYYY-MM-DD HH24:MI:SS'),
            'fungicida', :2, :3, :4
        )
    """
    data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute(sql, (data, quantidade_total, nome_produto, cd_area))


def listar_fungicidas(cursor):
    cursor.execute("""
        SELECT cd_aplicacao, dt_aplicacao, vl_quantidade,
               nm_produto, cd_area
        FROM Aplicacao
        WHERE tp_aplicacao = 'fungicida'
        ORDER BY dt_aplicacao DESC
    """)
    return cursor.fetchall()


def atualizar_fungicida(cursor, cd_aplicacao, nova_quantidade, nome_produto):
    sql = """
        UPDATE Aplicacao
        SET vl_quantidade = :1,
            nm_produto = :2
        WHERE cd_aplicacao = :3 AND tp_aplicacao = 'fungicida'
    """
    cursor.execute(sql, (nova_quantidade, nome_produto, cd_aplicacao))


def deletar_fungicida(cursor, cd_aplicacao):
    cursor.execute("""
        DELETE FROM Aplicacao
        WHERE cd_aplicacao = :1 AND tp_aplicacao = 'fungicida'
    """, (cd_aplicacao,))
