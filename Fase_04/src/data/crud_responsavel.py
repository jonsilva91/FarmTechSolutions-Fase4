'''CRUD de Responsável adaptado para SQLite'''

def inserir_responsavel(cursor, responsavel):
    """
    Insere um novo responsável.
    `responsavel` deve ser um dict com chaves: nm_responsavel, nm_telefone, nm_email
    """
    sql = '''
        INSERT INTO Responsavel (
            nm_responsavel, nm_telefone, nm_email
        ) VALUES (?, ?, ?)
    '''
    cursor.execute(sql, (
        responsavel['nm_responsavel'],
        responsavel['nm_telefone'],
        responsavel['nm_email']
    ))


def listar_responsaveis(cursor):
    """
    Retorna todos os responsáveis.
    """
    cursor.execute(
        '''
        SELECT cd_responsavel, nm_responsavel, nm_telefone, nm_email
        FROM Responsavel
        ORDER BY cd_responsavel
        '''
    )
    return cursor.fetchall()


def atualizar_responsavel(cursor, cd_responsavel, responsavel):
    """
    Atualiza dados de um responsável existente.
    """
    sql = '''
        UPDATE Responsavel
        SET nm_responsavel = ?, nm_telefone = ?, nm_email = ?
        WHERE cd_responsavel = ?
    '''
    cursor.execute(sql, (
        responsavel['nm_responsavel'],
        responsavel['nm_telefone'],
        responsavel['nm_email'],
        cd_responsavel
    ))


def deletar_responsavel(cursor, cd_responsavel):
    """
    Deleta um responsável pelo seu código.
    """
    cursor.execute(
        "DELETE FROM Responsavel WHERE cd_responsavel = ?",
        (cd_responsavel,)
    )