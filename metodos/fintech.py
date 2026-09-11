from abc import ABC, abstractmethod


# Classe ContaBancaria, usei o ABC Method
class ContaBancaria(ABC):
    """
    Criando conta bancaria para uma Fintech
    """

    def __init__(self, titular: str, saldo: float = 0, id: int = None):
        self.id = id
        self._titular = titular
        self.__saldo = saldo
        self.movimentacoes = []

    @abstractmethod
    def depositar(self, valor):
        try:
            valor = float(valor)
            valor = abs(valor)
            self.__saldo += valor
            self.movimentacoes.append(f"Depósito de: R$ {valor:,.2f}")
            print(f"Depósito de R${valor:,.2f} autorizado na conta {self._titular}.")
            return True
        except ValueError:
            print("Erro no depósito: O valor informado deve ser um número.")
            return False

    @abstractmethod
    def sacar(self, valor):
        # Aqui coloquei um try pra mensagem de erro, no terminal.
        try:
            valor = float(valor)
            valor = abs(valor)

            if valor > self.__saldo:
                print(
                    f"Saque NEGADO de R${valor:,.2f} "
                    f"na conta {self._titular}: SALDO INSUFICIENTE."
                )

                return False

            else:
                self.__saldo -= valor
                self.movimentacoes.append(f"Saque de: R$ {valor:,.2f}")

                print(
                    f"Saque de R${valor:,.2f} autorizado " f"na conta {self._titular}."
                )

                return True

        except ValueError:
            print("Erro ao sacar: O valor informado deve ser um número.")
            return False

    # property pra poder usar o saldo.
    @property
    def saldo(self):
        return self.__saldo

    # property pra poder usar o titular.
    @property
    def titular(self):
        return self._titular

    # Método str pra mensagem principal.
    def __str__(self):
        return f"Conta: {self.titular} - Saldo: R${self.saldo}"

    def exibir_extrato(self):
        print(f"Extrato da conta {self.titular}:")
        for movimento in self.movimentacoes:
            print(movimento)
        print(f"Saldo atual: R$ {self.__saldo:,.2f}")

    # Função interna open() Gerenciador de Contexto
    def exportar_extrato(self):
        with open(f"extrato_{self.titular}.txt", "w", encoding="utf-8") as arquivo:
            for movimento in self.movimentacoes:
                arquivo.write(movimento + "\n")


# Criei uma classe ContaEmpresarial, ela cobra uma taxa de 5 reais pra cada saque.
class ContaEmpresarial(ContaBancaria):

    def __init__(self, titular, saldo=0, id=None):
        super().__init__(titular, saldo, id)

    def depositar(self, valor):
        valor = float(valor)
        valor = abs(valor)
        return super().depositar(valor)

    def sacar(self, valor: float, taxa: float = 5):
        try:
            valor = float(valor)
            valor_total = abs(valor) + taxa
            return super().sacar(valor_total)

        except ValueError:
            print("Erro ao sacar: O valor informado deve ser um número.")
            return False


# Criei uma classe poupança pra pratica.
class ContaPoupanca(ContaBancaria):

    def __init__(self, titular, saldo=0, id=None, taxa_rendimento=0.01):
        super().__init__(titular, saldo, id)
        self.taxa_rendimento = taxa_rendimento

    def depositar(self, valor):
        try:
            valor = float(valor)
            valor = abs(valor)
            valor_rendimento = valor + (valor * self.taxa_rendimento)
            return super().depositar(valor_rendimento)
        except ValueError:
            print("Erro no depósito: O valor informado deve ser um número.")
            return False

    def sacar(self, valor: float, taxa: float = 1):
        valor = float(valor)
        valor_total = abs(valor) + taxa
        return super().sacar(valor_total)
