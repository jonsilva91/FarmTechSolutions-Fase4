from datetime import datetime

def inserir_adubacao(cursor, cd_area, fosforo, potassio, nitrogenio):
    """
    Registra uma adubação na tabela Aplicacao.
    """
    sql = """
        INSERT INTO Aplicacao (
            cd_aplicacao, dt_aplicacao, tp_aplicacao,
            vl_quantidade, vl_fosforo, vl_potassio, vl_nitrogenio, cd_area
        ) VALUES (
            (SELECT NVL(MAX(cd_aplicacao), 0) + 1 FROM Aplicacao),
            TO_DATE(:1, 'YYYY-MM-DD HH24:MI:SS'),
            'adubacao', :2, :3, :4, :5, :6
        )
    """
    total = sum(v for v in [fosforo, potassio, nitrogenio] if v is not None)
    data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute(sql, (data, total, fosforo, potassio, nitrogenio, cd_area))


def listar_adubacoes(cursor):
    cursor.execute("""
        SELECT cd_aplicacao, dt_aplicacao, vl_quantidade,
               vl_fosforo, vl_potassio, vl_nitrogenio, cd_area
        FROM Aplicacao
        WHERE tp_aplicacao = 'adubacao'
        ORDER BY dt_aplicacao DESC
    """)
    return cursor.fetchall()


def atualizar_adubacao(cursor, cd_aplicacao, fosforo, potassio, nitrogenio):
    total = sum(v for v in [fosforo, potassio, nitrogenio] if v is not None)
    sql = """
        UPDATE Aplicacao
        SET vl_quantidade = :1,
            vl_fosforo = :2,
            vl_potassio = :3,
            vl_nitrogenio = :4
        WHERE cd_aplicacao = :5 AND tp_aplicacao = 'adubacao'
    """
    cursor.execute(sql, (total, fosforo, potassio, nitrogenio, cd_aplicacao))


def deletar_adubacao(cursor, cd_aplicacao):
    cursor.execute("""
        DELETE FROM Aplicacao
        WHERE cd_aplicacao = :1 AND tp_aplicacao = 'adubacao'
    """, (cd_aplicacao,))
