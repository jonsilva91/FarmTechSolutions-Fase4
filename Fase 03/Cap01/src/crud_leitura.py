
def inserir_leitura(cursor, cd_sensor, dt_leitura, valor):
    cursor.execute("""
        INSERT INTO Leitura_Sensor (
            cd_sensor, dt_leitura, vl_valor
        ) VALUES (:1, TO_DATE(:2, 'YYYY-MM-DD HH24:MI:SS'), :3)
    """, (cd_sensor, dt_leitura, valor))

def listar_leituras(cursor):
    cursor.execute("SELECT * FROM Leitura_Sensor")
    return cursor.fetchall()

def atualizar_leitura(cursor, cd_leitura, novo_valor):
    cursor.execute("UPDATE Leitura_Sensor SET vl_valor = :1 WHERE cd_leitura = :2", (novo_valor, cd_leitura))

def deletar_leitura(cursor, cd_leitura):
    cursor.execute("DELETE FROM Leitura_Sensor WHERE cd_leitura = :1", (cd_leitura,))
