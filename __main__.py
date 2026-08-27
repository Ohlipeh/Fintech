from fintech import ContaEmpresarial
from banco import ContaBancariaRepository, Database
from rich.console import Console
from rich.prompt import Prompt

from interface import iniciar_interface

console = Console()


def main():

    # Conectar ao banco
    db = Database()
    conexao = db.conectar()

    cb_repo = ContaBancariaRepository(db)

    # Criar Tabelas
    cb_repo.criar_tabelas()

    console.print("[bold green]Sistema iniciado com sucesso![/bold green]")

    # Criamos uma conta para testes
    titular = Prompt.ask("Digite o nome do titular da conta")
    cb = ContaEmpresarial(titular)
    cb_repo.salvar_conta(cb)
    iniciar_interface(cb, cb_repo)


if __name__ == "__main__":
    main()
