'''CRUD de Sensor adaptado para SQLite'''

def inserir_sensor(cursor, tp_sensor, nm_modelo, cd_area):
    """
    Insere um novo sensor e retorna o ID gerado.
    """
    sql = '''
        INSERT INTO Sensor (
            tp_sensor, nm_modelo, cd_area
        ) VALUES (?, ?, ?)
    '''
    cursor.execute(sql, (tp_sensor, nm_modelo, cd_area))
    return cursor.lastrowid


def listar_sensores(cursor):
    """
    Retorna todos os sensores.
    """
    cursor.execute(
        '''
        SELECT cd_sensor, tp_sensor, nm_modelo, cd_area
        FROM Sensor
        ORDER BY cd_sensor
        '''
    )
    return cursor.fetchall()


def atualizar_sensor(cursor, cd_sensor, tp_sensor=None, nm_modelo=None, cd_area=None):
    """
    Atualiza campos de um sensor existente.
    Só atualiza parâmetros não None.
    """
    updates = []
    params = []
    if tp_sensor is not None:
        updates.append('tp_sensor = ?')
        params.append(tp_sensor)
    if nm_modelo is not None:
        updates.append('nm_modelo = ?')
        params.append(nm_modelo)
    if cd_area is not None:
        updates.append('cd_area = ?')
        params.append(cd_area)
    params.append(cd_sensor)
    sql = f"UPDATE Sensor SET {', '.join(updates)} WHERE cd_sensor = ?"
    cursor.execute(sql, tuple(params))


def deletar_sensor(cursor, cd_sensor):
    """
    Deleta um sensor pelo seu código.
    """
    cursor.execute(
        "DELETE FROM Sensor WHERE cd_sensor = ?",
        (cd_sensor,)
    )
