from datetime import datetime

# CRUD de Adubação adaptado para SQLite

def inserir_adubacao(cursor, cd_area, fosforo, potassio, nitrogenio):
    """
    Registra uma adubação na tabela Aplicacao (SQLite).
    """
    sql = """
        INSERT INTO Aplicacao (
            dt_aplicacao, tp_aplicacao,
            vl_quantidade, vl_fosforo, vl_potassio, vl_nitrogenio, cd_area
        ) VALUES (?, ?, ?, ?, ?, ?, ?)
    """
    total = sum(v for v in [fosforo, potassio, nitrogenio] if v is not None)
    data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute(sql, (data, 'adubacao', total, fosforo, potassio, nitrogenio, cd_area))


def listar_adubacoes(cursor):
    """
    Retorna todas as adubações, ordenadas pela data (DESC).
    """
    cursor.execute(
        """
        SELECT cd_aplicacao, dt_aplicacao, vl_quantidade,
               vl_fosforo, vl_potassio, vl_nitrogenio, cd_area
        FROM Aplicacao
        WHERE tp_aplicacao = 'adubacao'
        ORDER BY dt_aplicacao DESC
        """
    )
    return cursor.fetchall()


def atualizar_adubacao(cursor, cd_aplicacao, fosforo, potassio, nitrogenio):
    """
    Atualiza valores de adubação existente.
    """
    total = sum(v for v in [fosforo, potassio, nitrogenio] if v is not None)
    sql = """
        UPDATE Aplicacao
        SET vl_quantidade = ?,
            vl_fosforo = ?,
            vl_potassio = ?,
            vl_nitrogenio = ?
        WHERE cd_aplicacao = ? AND tp_aplicacao = 'adubacao'
    """
    cursor.execute(sql, (total, fosforo, potassio, nitrogenio, cd_aplicacao))


def deletar_adubacao(cursor, cd_aplicacao):
    """
    Remove um registro de adubação.
    """
    cursor.execute(
        """
        DELETE FROM Aplicacao
        WHERE cd_aplicacao = ? AND tp_aplicacao = 'adubacao'
        """,
        (cd_aplicacao,)
    )
