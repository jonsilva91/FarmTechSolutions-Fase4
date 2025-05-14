
def inserir_adubacao(cursor, cd_cultura, tipo, fosforo, potassio, nitrogenio=None):
    cursor.execute("""
        INSERT INTO Adubacao (
            cd_cultura, ds_tipo, vl_fosforo, vl_potassio, vl_nitrogenio
        ) VALUES (:1, :2, :3, :4, :5)
    """, (cd_cultura, tipo, fosforo, potassio, nitrogenio))

def listar_adubacoes(cursor):
    cursor.execute("SELECT * FROM Adubacao")
    return cursor.fetchall()

def atualizar_adubacao(cursor, cd_adubacao, fosforo, potassio, nitrogenio):
    cursor.execute("""
        UPDATE Adubacao
        SET vl_fosforo = :1, vl_potassio = :2, vl_nitrogenio = :3
        WHERE cd_adubacao = :4
    """, (fosforo, potassio, nitrogenio, cd_adubacao))

def deletar_adubacao(cursor, cd_adubacao):
    cursor.execute("DELETE FROM Adubacao WHERE cd_adubacao = :1", (cd_adubacao,))
