
def inserir_cultura(cursor, cultura):
    cursor.execute("""
        INSERT INTO Cultura (
            nm_cultura, vl_area, vl_densidade, vl_espacamento,
            vl_taxa_semeadura, vl_peso_hectare, ds_produtividade
        ) VALUES (:1, :2, :3, :4, :5, :6, :7)
    """, (
        cultura["nm_cultura"], cultura["vl_area"], cultura["vl_densidade"],
        cultura["vl_espacamento"], cultura["vl_taxa_semeadura"],
        cultura["vl_peso_hectare"], cultura["ds_produtividade"]
    ))

def listar_culturas(cursor):
    cursor.execute("SELECT * FROM Cultura")
    return cursor.fetchall()

def atualizar_area(cursor, id_cultura, nova_area):
    cursor.execute("UPDATE Cultura SET vl_area = :1 WHERE cd_cultura = :2", (nova_area, id_cultura))

def deletar_cultura(cursor, id_cultura):
    cursor.execute("DELETE FROM Cultura WHERE cd_cultura = :1", (id_cultura,))
