'''CRUD de Cultura adaptado para SQLite'''

def inserir_cultura(cursor, cultura):
    """
    Insere uma nova cultura na tabela Cultura.
    Espera um dict `cultura` com as chaves: nm_cultura, tp_cultura
    """
    sql = '''
        INSERT INTO Cultura (
            nm_cultura, tp_cultura
        ) VALUES (?, ?)
    '''
    cursor.execute(sql, (
        cultura["nm_cultura"],
        cultura["tp_cultura"]
    ))


def listar_culturas_com_area(cursor):
    """
    Retorna lista de culturas com dados de área de plantio (LEFT JOIN).
    """
    cursor.execute(
        '''
        SELECT
            c.cd_cultura,
            c.nm_cultura,
            c.tp_cultura,
            a.vl_area_ha,
            a.vl_espacamento,
            a.vl_densidade,
            a.vl_taxa_semeadura,
            a.vl_peso_ha,
            a.ds_produtividade,
            a.cd_area
        FROM Cultura c
        LEFT JOIN Area_Plantio a ON c.cd_cultura = a.cd_cultura
        '''
    )
    return cursor.fetchall()


def atualizar_area(cursor, nova_area, cd_cultura):
    """
    Atualiza o valor de área (vl_area_ha) em Area_Plantio para uma dada cultura.
    """
    sql = 'UPDATE Area_Plantio SET vl_area_ha = ? WHERE cd_cultura = ?'
    cursor.execute(sql, (nova_area, cd_cultura))


def deletar_cultura(cursor, id_cultura):
    """
    Remove uma cultura pelo seu código.
    """
    sql = 'DELETE FROM Cultura WHERE cd_cultura = ?'
    cursor.execute(sql, (id_cultura,))
