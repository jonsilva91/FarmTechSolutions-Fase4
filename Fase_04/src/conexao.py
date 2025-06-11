from dotenv import load_dotenv
import os
import oracledb

load_dotenv()  # Carrega variáveis do .env

class OracleDB:
    def __init__(self):
        self.conn = oracledb.connect(
            user=os.getenv("ORACLE_USER"),
            password=os.getenv("ORACLE_PASSWORD"),
            dsn=os.getenv("ORACLE_DSN")
        )
        self.cursor = self.conn.cursor()

    def fechar(self):
        self.cursor.close()
        self.conn.close()
