# Importação do SQLite
import sqlite3


# Classe Databebase para conectar e desconectar o banco
class Database:

    def conectar(self):
        self.conexao = sqlite3.connect("fintech.db")
        self.conexao.execute("PRAGMA foreign_keys = ON")
        return self.conexao

    def desconectar(self):
        self.conexao.close()
        print("CONEXÃO ENCERRADA!")


# Classe Repository para criar as tabelas, futuramente pretendo colocar mais tabelas pra ficar completo, mas atualemnte vai ficar assim só pra teste.
class Repository:

    def __init__(self, database):
        self.db = database


class ContaBancariaRepository(Repository):

    def criar_tabelas(self):
        cursor = self.db.conexao.cursor()
        cursor.execute("""
                CREATE TABLE IF NOT EXISTS contas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    titular TEXT NOT NULL,
                    saldo REAL NOT NULL,
                    taxa_rendimento REAL NOT NULL
                )
            """)
        self.db.conexao.commit()

    def salvar_conta(self, conta):
        cursor = self.db.conexao.cursor()
        cursor.execute(
            """
                    INSERT INTO contas (titular, saldo, taxa_rendimento)
                    VALUES (?, ?, ?)
            """,
            (conta.titular, conta.saldo, conta.taxa_rendimento),
        )
        conta.id = cursor.lastrowid
        self.db.conexao.commit()

    def atualizar_conta(self, conta):
        cursor = self.db.conexao.cursor()

        cursor.execute(
            """
            UPDATE contas
            SET titular = ?, saldo = ?, taxa_rendimento = ?
            WHERE id = ?
            """,
            (conta.titular, conta.saldo, conta.taxa_rendimento, conta.id),
        )

        self.db.conexao.commit()
