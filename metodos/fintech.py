class ContaBancaria:
    """
    Criando conta bancaria para uma Fintech
    """

    def __init__(self, titular: str, saldo: float = 0, id: int = None):
        self.id = id
        self._titular = titular
        self.__saldo = saldo
        self.movimentacoes = []

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

    def sacar(self, valor):
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

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self._titular

    def __str__(self):
        return f"Conta Empresarial de {self.titular} - Saldo: R${self.saldo}"

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


class ContaEmpresarial(ContaBancaria):

    def __init__(self, titular, saldo=0, id=None):
        super().__init__(titular, saldo, id)

    def sacar(self, valor: float, taxa: float = 5):
        try:
            valor = float(valor)
            valor_total = abs(valor) + taxa
            return super().sacar(valor_total)

        except ValueError:
            print("Erro ao sacar: O valor informado deve ser um número.")
            return False
