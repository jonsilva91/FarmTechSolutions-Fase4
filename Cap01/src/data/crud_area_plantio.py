
def inserir_area_plantio(cursor, area):
    sql = """
        INSERT INTO Area_Plantio (
            cd_area, vl_area_ha, vl_espacamento, vl_densidade,
            vl_taxa_semeadura, vl_peso_ha, cd_cultura, cd_responsavel, ds_produtividade
        ) VALUES (:1, :2, :3, :4, :5, :6, :7, :8, :9)
    """
    ds_prod = area["ds_produtividade"]
    if not ds_prod:
        ds_prod = None  # Garante que seja NULL válido
    cursor.execute(sql, (
        area["cd_area"],
        area["vl_area_ha"],
        area["vl_espacamento"],
        area["vl_densidade"],
        area["vl_taxa_semeadura"],
        area["vl_peso_ha"],
        area["cd_cultura"],
        area["cd_responsavel"],
        ds_prod
    ))
