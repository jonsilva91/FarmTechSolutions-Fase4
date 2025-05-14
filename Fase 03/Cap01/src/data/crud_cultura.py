
def inserir_cultura(cursor, cultura):
    sql = """
        INSERT INTO Cultura (
            cd_cultura, nm_cultura, tp_cultura
        ) VALUES (:1, :2, :3)
    """
    cursor.execute(sql, (
        cultura["cd_cultura"],
        cultura["nm_cultura"],
        cultura["tp_cultura"]
    ))

def listar_culturas_com_area(cursor):
    cursor.execute("""
        SELECT 
            c.cd_cultura, 
            c.nm_cultura, 
            c.tp_cultura,
            a.vl_area_ha,
            a.vl_espacamento,
            a.vl_densidade,
            a.vl_taxa_semeadura,
            a.vl_peso_ha,
            a.ds_produtividade
        FROM Cultura c
        JOIN Area_Plantio a ON c.cd_cultura = a.cd_cultura
    """)
    return cursor.fetchall()

def atualizar_area(cursor, id_cultura, nova_area):
    cursor.execute("UPDATE Cultura SET vl_area = :1 WHERE cd_cultura = :2", (nova_area, id_cultura))

def deletar_cultura(cursor, id_cultura):
    cursor.execute("DELETE FROM Cultura WHERE cd_cultura = :1", (id_cultura,))
