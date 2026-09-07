from metodos.fintech import ContaBancaria


class ControladorFinanceiro:

    def __init__(self, cb, cb_repo):
        self.cb = cb
        self.cb_repo = cb_repo

    def processar_deposito(self, valor_digitado):

        if self.cb.depositar(valor_digitado):
            self.cb_repo.atualizar_conta(self.cb)
            return True, f"Saldo atual: R$ {self.cb.saldo:.2f}"
        else:
            return False, "VALOR INVÁLIDO para depósito!"

    def processar_saque(self, valor_digitado):

        if self.cb.sacar(valor_digitado):
            self.cb_repo.atualizar_conta(self.cb)
            return True, f"Saldo atual: R$ {self.cb.saldo:.2f}"
        else:
            return False, "VALOR INVÁLIDO para saque!"

    def obter_saldo_inicial(self):
        saldo_inicial = self.cb.saldo
        return f"Saldo atual: R${saldo_inicial:.2f}."

    def obter_extrato(self):
        return self.cb.movimentacoes

    def processar_exportacao(self):
        try:
            self.cb.exportar_extrato()
            return True, "Extrato exportado com sucesso!"
        except Exception as e:
            return False, f"Erro ao exportar extrato: {e}"
