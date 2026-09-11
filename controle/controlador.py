from metodos.fintech import ContaEmpresarial, ContaPoupanca


class ControladorFinanceiro:

    def __init__(self, cb, cb_repo):
        self.cb = cb
        self.cb_repo = cb_repo
        self.conta_ativa = None

    def processar_criacao_conta(self, titular, tipo_conta):
        if self.conta_ativa:
            return False, "Já existe uma conta ativa."
        if tipo_conta == "empresarial":
            self.conta_ativa = ContaEmpresarial(titular)
        elif tipo_conta == "poupanca":
            self.conta_ativa = ContaPoupanca(titular)
        else:
            return False, "Tipo de conta inválido."

        # Atualiza cb para apontar para a conta ativa
        self.cb = self.conta_ativa

        # Salva no repositório
        if self.cb_repo:
            self.cb_repo.salvar_conta(self.conta_ativa)

        return (
            True,
            f"Conta {tipo_conta} criada para {titular} com saldo inicial R$ {self.conta_ativa.saldo:.2f}",
        )

    def processar_deposito(self, valor_digitado):

        # Se não há conta ativa, não pode depositar
        if not self.conta_ativa:
            return False, f"Erro: Nenhuma conta foi ativada. Crie uma conta primeiro!"

        # Se há conta ativa, tenta depositar
        if self.cb.depositar(valor_digitado):
            self.cb_repo.atualizar_conta(self.cb)
            return True, f"Saldo atual: R$ {self.conta_ativa.saldo:.2f}"
        else:
            return False, "VALOR INVÁLIDO para depósito!"

    def processar_saque(self, valor_digitado):

        # Se não há conta ativa, não pode sacar.
        if not self.conta_ativa:
            return False, f"Erro: Nenhuma conta foi ativada. Crie uma conta primeiro!"

        # Se há conta ativa, tenta sacar.
        if self.cb.sacar(valor_digitado):
            self.cb_repo.atualizar_conta(self.cb)
            return True, f"Saldo atual: R$ {self.conta_ativa.saldo:.2f}"
        else:
            return False, "VALOR INVÁLIDO para saque!"

    def obter_saldo_inicial(self):
        if not self.cb:
            return "Nenhuma conta ativa."
        saldo_inicial = self.cb.saldo
        return f"Saldo atual: R${saldo_inicial:.2f}."

    def obter_extrato(self):
        return self.conta_ativa.movimentacoes

    def processar_exportacao(self):
        try:
            self.cb.exportar_extrato()
            return True, "Extrato exportado com sucesso!"
        except Exception as e:
            return False, f"Erro ao exportar extrato: {e}"
