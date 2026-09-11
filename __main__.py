# Imports
from banco_dados.banco import ContaBancariaRepository, Database
from controle.controlador import ControladorFinanceiro
from interface.interface import iniciar_interface

from rich.console import Console

console = Console()


def main():
    # Conectar ao banco
    db = Database()
    conexao = db.conectar()

    cb_repo = ContaBancariaRepository(db)

    # Criar tabelas
    cb_repo.criar_tabelas()

    console.print("[bold green]Sistema iniciado com sucesso![/bold green]")

    # Inicializa o controlador sem conta ativa
    controlador = ControladorFinanceiro(cb=None, cb_repo=cb_repo)

    # Inicia interface gráfica
    iniciar_interface(controlador)


if __name__ == "__main__":
    main()
