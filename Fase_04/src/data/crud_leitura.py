'''CRUD de Leitura de Sensor adaptado para SQLite'''

def inserir_leitura(cursor, cd_sensor, dt_leitura, valor):
    """
    Insere uma nova leitura na tabela Leitura_Sensor.
    Espera dt_leitura como string 'YYYY-MM-DD HH:MM:SS' ou datetime.
    """
    sql = '''
        INSERT INTO Leitura_Sensor (
            cd_sensor, dt_leitura, vl_valor
        ) VALUES (?, ?, ?)
    '''
    # Se dt_leitura for datetime, convert para string
    try:
        # dt_leitura tem método strftime?
        dt_str = dt_leitura.strftime("%Y-%m-%d %H:%M:%S")
    except AttributeError:
        dt_str = dt_leitura
    cursor.execute(sql, (cd_sensor, dt_str, valor))


def listar_leituras(cursor):
    """
    Retorna todas as leituras de sensor.
    """
    cursor.execute(
        '''
        SELECT cd_leitura, cd_sensor, dt_leitura, vl_valor
        FROM Leitura_Sensor
        ORDER BY dt_leitura DESC
        '''
    )
    return cursor.fetchall()


def atualizar_leitura(cursor, cd_leitura, novo_valor):
    """
    Atualiza o valor de uma leitura pelo seu código.
    """
    sql = 'UPDATE Leitura_Sensor SET vl_valor = ? WHERE cd_leitura = ?'
    cursor.execute(sql, (novo_valor, cd_leitura))


def deletar_leitura(cursor, cd_leitura):
    """
    Deleta uma leitura de sensor pelo seu código.
    """
    sql = 'DELETE FROM Leitura_Sensor WHERE cd_leitura = ?'
    cursor.execute(sql, (cd_leitura,))
