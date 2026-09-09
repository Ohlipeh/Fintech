# Aqui está os imports de todos os arquivos necessários.
from banco_dados.banco import ContaBancariaRepository, Database
from controle.controlador import ControladorFinanceiro
from metodos.fintech import ContaEmpresarial, ContaPoupanca
from interface.interface import iniciar_interface

# Fiz um import de rich pra deixar o terminal mais organizado.
from rich.console import Console
from rich.prompt import Prompt

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
    cb = ContaEmpresarial("Sua Empresa")
    cb = ContaPoupanca(titular)
    controlador = ControladorFinanceiro(cb, cb_repo)
    cb_repo.salvar_conta(cb)

    iniciar_interface(controlador)


if __name__ == "__main__":
    main()
