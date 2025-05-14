
def inserir_fungicida(cursor, cd_cultura, nome, dosagem, qt_pulverizadores, fungicida_ha, total_fungicida):
    cursor.execute("""
        INSERT INTO Fungicida (
            cd_cultura, nm_fungicida, vl_dosagem, qt_pulverizadores,
            vl_fungicida_ha, vl_total_fungicida
        ) VALUES (:1, :2, :3, :4, :5, :6)
    """, (cd_cultura, nome, dosagem, qt_pulverizadores, fungicida_ha, total_fungicida))

def listar_fungicidas(cursor):
    cursor.execute("SELECT * FROM Fungicida")
    return cursor.fetchall()

def atualizar_fungicida(cursor, cd_fungicida, dosagem, qt_pulverizadores):
    cursor.execute("""
        UPDATE Fungicida
        SET vl_dosagem = :1, qt_pulverizadores = :2
        WHERE cd_fungicida = :3
    """, (dosagem, qt_pulverizadores, cd_fungicida))

def deletar_fungicida(cursor, cd_fungicida):
    cursor.execute("DELETE FROM Fungicida WHERE cd_fungicida = :1", (cd_fungicida,))
