import sqlite3


class Database:

    def conectar(self):
        self.conexao = sqlite3.connect("fintech.db")
        self.conexao.execute("PRAGMA foreign_keys = ON")
        return self.conexao

    def desconectar(self):
        self.conexao.close()
        print("CONEXÃO ENCERRADA!")


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
                    saldo REAL NOT NULL
                )
            """)
        self.db.conexao.commit()

    def salvar_conta(self, conta):
        cursor = self.db.conexao.cursor()
        cursor.execute(
            """
                    INSERT INTO contas (titular, saldo)
                    VALUES (?, ?)
            """,
            (conta.titular, conta.saldo),
        )
        conta.id = cursor.lastrowid
        self.db.conexao.commit()

    def atualizar_conta(self, conta):
        cursor = self.db.conexao.cursor()

        cursor.execute(
            """
            UPDATE contas
            SET titular = ?, saldo = ?
            WHERE id = ?
            """,
            (conta.titular, conta.saldo, conta.id),
        )

        self.db.conexao.commit()
