# Importação do SQLite
import sqlite3

from fintech import ContaEmpresarial, ContaPoupanca


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
                    tipo_conta TEXT NOT NULL,
                    taxa_rendimento REAL
                    
                )
            """)
        self.db.conexao.commit()

    def salvar_conta(self, conta):
        # Descobre o nome da classe do objeto
        nome_da_classe = conta.__class__.__name__
        # Só le taxa_rendimento se for ContaPoupança
        if nome_da_classe == "ContaPoupanca":
            taxa_para_salvar = conta.taxa_rendimento
        else:
            taxa_para_salvar = None

        cursor = self.db.conexao.cursor()
        cursor.execute(
            """
                    INSERT INTO contas (titular, saldo, tipo_conta, taxa_rendimento)
                    VALUES (?, ?, ?, ?)
            """,
            (
                conta.titular,
                conta.saldo,
                nome_da_classe,
                taxa_para_salvar,
            ),
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

    def buscar_por_id(self, id_conta):
        cursor = self.db.conexao.cursor()
        cursor.execute(
            """
            SELECT id, titular, saldo, tipo_conta, taxa_rendimento
            FROM contas
            WHERE id = ?
            """,
            (id_conta,),
        )

        return cursor.fetchone()

    def buscar_todas(self):
        cursor = self.db.conexao.cursor()
        cursor.execute(
            "SELECT id, titular, saldo, tipo_conta, taxa_rendimento FROM contas"
        )

        resultado = cursor.fetchall()

        contas = []

        for linha in resultado:
            if linha[3] == "ContaPoupanca":
                conta = ContaPoupanca(linha[1], linha[2], linha[4])
            elif linha[3] == "ContaEmpresarial":
                conta = ContaEmpresarial(linha[1], linha[2])
            else:
                raise ValueError(f"Tipo de conta desconhecido: {linha[3]}")

            conta.id = linha[0]
            contas.append(conta)

        return contas
