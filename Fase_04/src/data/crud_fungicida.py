from datetime import datetime

'''CRUD de Fungicida adaptado para SQLite'''

def inserir_fungicida(cursor, cd_area, quantidade_total, nome_produto):
    """
    Registra uma aplicação de fungicida na tabela Aplicacao (SQLite).
    """
    sql = '''
        INSERT INTO Aplicacao (
            dt_aplicacao, tp_aplicacao,
            vl_quantidade, nm_produto, cd_area
        ) VALUES (?, ?, ?, ?, ?)
    '''
    data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute(sql, (
        data,
        'fungicida',
        quantidade_total,
        nome_produto,
        cd_area
    ))


def listar_fungicidas(cursor):
    """
    Retorna todas as aplicações de fungicida, ordenadas pela data (DESC).
    """
    cursor.execute(
        '''
        SELECT cd_aplicacao, dt_aplicacao, vl_quantidade,
               nm_produto, cd_area
        FROM Aplicacao
        WHERE tp_aplicacao = 'fungicida'
        ORDER BY dt_aplicacao DESC
        '''
    )
    return cursor.fetchall()


def atualizar_fungicida(cursor, cd_aplicacao, nova_quantidade, nome_produto):
    """
    Atualiza valores de fungicida existente.
    """
    sql = '''
        UPDATE Aplicacao
        SET vl_quantidade = ?,
            nm_produto = ?
        WHERE cd_aplicacao = ? AND tp_aplicacao = 'fungicida'
    '''
    cursor.execute(sql, (nova_quantidade, nome_produto, cd_aplicacao))


def deletar_fungicida(cursor, cd_aplicacao):
    """
    Remove um registro de fungicida.
    """
    cursor.execute(
        '''
        DELETE FROM Aplicacao
        WHERE cd_aplicacao = ? AND tp_aplicacao = 'fungicida'
        '''
        , (cd_aplicacao,)
    )
