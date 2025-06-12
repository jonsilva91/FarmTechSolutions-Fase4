'''CRUD de Área de Plantio adaptado para SQLite'''

def inserir_area_plantio(cursor, area):
    """
    Insere uma nova área de plantio na tabela Area_Plantio.
    Espera um dict `area` com as chaves:
    - vl_area_ha, vl_espacamento, vl_densidade,
      vl_taxa_semeadura, vl_peso_ha, cd_cultura, cd_responsavel, ds_produtividade
    """
    sql = '''
        INSERT INTO Area_Plantio (
            vl_area_ha, vl_espacamento, vl_densidade,
            vl_taxa_semeadura, vl_peso_ha, cd_cultura,
            cd_responsavel, ds_produtividade
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    '''
    ds_prod = area.get("ds_produtividade") or None
    params = (
        area["vl_area_ha"],
        area["vl_espacamento"],
        area["vl_densidade"],
        area["vl_taxa_semeadura"],
        area["vl_peso_ha"],
        area["cd_cultura"],
        area["cd_responsavel"],
        ds_prod
    )
    cursor.execute(sql, params)


def listar_area_plantio(cursor):
    """
    Retorna todas as áreas de plantio, ordenadas pelo ID decrescente.
    """
    cursor.execute(
        '''
        SELECT cd_area, vl_area_ha, vl_espacamento, vl_densidade,
               vl_taxa_semeadura, vl_peso_ha, cd_cultura,
               cd_responsavel, ds_produtividade
        FROM Area_Plantio
        ORDER BY cd_area DESC
        '''
    )
    return cursor.fetchall()


def atualizar_area_plantio(cursor, cd_area, area):
    """
    Atualiza os dados de uma área de plantio existente.
    `area` é um dict com os mesmos campos do insert.
    """
    sql = '''
        UPDATE Area_Plantio
        SET vl_area_ha = ?,
            vl_espacamento = ?,
            vl_densidade = ?,
            vl_taxa_semeadura = ?,
            vl_peso_ha = ?,
            cd_cultura = ?,
            cd_responsavel = ?,
            ds_produtividade = ?
        WHERE cd_area = ?
    '''
    ds_prod = area.get("ds_produtividade") or None
    params = (
        area["vl_area_ha"],
        area["vl_espacamento"],
        area["vl_densidade"],
        area["vl_taxa_semeadura"],
        area["vl_peso_ha"],
        area["cd_cultura"],
        area["cd_responsavel"],
        ds_prod,
        cd_area
    )
    cursor.execute(sql, params)


def deletar_area_plantio(cursor, cd_area):
    """
    Deleta uma área de plantio pelo seu ID.
    """
    cursor.execute(
        '''
        DELETE FROM Area_Plantio
        WHERE cd_area = ?
        ''',
        (cd_area,)
    )
