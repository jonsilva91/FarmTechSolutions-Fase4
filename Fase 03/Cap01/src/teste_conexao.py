from conexao import OracleDB

def testar_conexao():
    try:
        db = OracleDB()
        db.cursor.execute("SELECT table_name FROM user_tables")
        tabelas = db.cursor.fetchall()
        print("✅ Tabelas encontradas no schema:")
        for t in tabelas:
            print("-", t[0])
        db.fechar()
    except Exception as e:
        print("❌ Erro na conexão:", e)

if __name__ == "__main__":
    testar_conexao()
