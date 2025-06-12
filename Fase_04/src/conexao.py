from pathlib import Path
import sqlite3

# Caminho para o banco SQLite
DB_PATH = Path(__file__).parent.parent / "config" / "farmtech.db"


class SQLiteDB:
    def __init__(self):
        # Conecta ao banco SQLite e configura row_factory para acesso por coluna
        self.conn = sqlite3.connect(DB_PATH)
        self.conn.row_factory = sqlite3.Row
        self.conn.execute("PRAGMA foreign_keys = ON;")
        self.cursor = self.conn.cursor()

    def fechar(self):
        """
        Fecha o cursor e a conexão com o banco de dados.
        """
        self.cursor.close()
        self.conn.close()

    def __enter__(self):
        # Permite uso em with-statement
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Garante fechamento ao sair do with-statement
        self.fechar()
