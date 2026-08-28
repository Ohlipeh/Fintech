import customtkinter as ctk
from metodos.fintech import ContaBancaria


def mensagem_erro(mensagem):
    janela_erro = ctk.CTkToplevel()
    janela_erro.title("Erro")
    janela_erro.geometry("250x150")

    label = ctk.CTkLabel(janela_erro, text=mensagem)
    label.pack(pady=20)

    botao = ctk.CTkButton(janela_erro, text="OK", command=janela_erro.destroy)
    botao.pack(pady=10)


def iniciar_interface(cb, cb_repo):
    root = ctk.CTk()

    root.title("Sistema Fintech")
    root.geometry("500x500")

    titulo = ctk.CTkLabel(root, text="Sistema Fintech", font=("Arial", 28, "bold"))
    titulo.pack(pady=30)

    lbl_saldo = ctk.CTkLabel(
        root, text=f"Saldo atual: R$ {cb.saldo:.2f}", font=("Arial", 12, "bold")
    )
    lbl_saldo.pack()

    def acao_depositar():
        janela = ctk.CTkToplevel()
        janela.title("Depositar")
        janela.geometry("300x200")

        label = ctk.CTkLabel(janela, text="Digite o valor do depósito:")
        label.pack(pady=20)

        entrada = ctk.CTkEntry(janela, placeholder_text="Ex: 100.00")
        entrada.pack(pady=10)

        def confirmar_deposito():
            valor = entrada.get()
            if cb.depositar(valor):
                cb_repo.atualizar_conta(cb)
                print("Depósito salvo no banco!")
                lbl_saldo.configure(text=f"Saldo atual: R$ {cb.saldo:.2f}")
                janela.destroy()
            else:
                mensagem_erro("VALOR INVÁLIDO para depósito!")
                entrada.delete(0, "end")

        botao = ctk.CTkButton(janela, text="Depositar", command=confirmar_deposito)
        botao.pack(pady=10)

    def acao_sacar():
        janela = ctk.CTkToplevel()
        janela.title("Sacar")
        janela.geometry("300x200")

        label = ctk.CTkLabel(janela, text="Digite o valor a sacar:")
        label.pack(pady=20)

        entrada = ctk.CTkEntry(janela, placeholder_text="Ex: 100.00")
        entrada.pack(pady=10)

        def confirmar_saque():
            valor = entrada.get()
            if cb.sacar(valor):
                cb_repo.atualizar_conta(cb)
                print("Saque salvo no banco!")
                lbl_saldo.configure(text=f"Saldo atual: R$ {cb.saldo:.2f}")
                janela.destroy()
            else:
                mensagem_erro("VALOR INVÁLIDO para saque!")

        botao = ctk.CTkButton(janela, text="Sacar", command=confirmar_saque)
        botao.pack(pady=20)

    def acao_extrato():
        janela = ctk.CTkToplevel()
        janela.title("Extrato da conta")
        janela.geometry("400x400")

        entrada = ctk.CTkTextbox(janela, width=350, height=300)
        entrada.pack(pady=20)

        for movimento in cb.movimentacoes:
            entrada.insert("end", movimento + "\n")

        botao = ctk.CTkButton(janela, text="Fechar", command=janela.destroy)
        botao.pack(pady=20)

    def acao_exportar():
        janela = ctk.CTkToplevel()
        janela.title("Extrato")
        janela.geometry("250x150")

        label = ctk.CTkLabel(janela, text="Extrato exportado com sucesso!")
        label.pack(pady=20)

        cb.exportar_extrato()

        botao = ctk.CTkButton(janela, text="Ok", command=janela.destroy)
        botao.pack(pady=20)

    btn_depositar = ctk.CTkButton(root, text="Depositar", command=acao_depositar)
    btn_depositar.pack(pady=5)

    btn_sacar = ctk.CTkButton(root, text="Sacar", command=acao_sacar)
    btn_sacar.pack(pady=5)

    btn_extrato = ctk.CTkButton(root, text="Extrato", command=acao_extrato)
    btn_extrato.pack(pady=5)

    btn_exportar = ctk.CTkButton(root, text="Exportar Extrato", command=acao_exportar)
    btn_exportar.pack(pady=5)

    btn_sair = ctk.CTkButton(root, text="Sair", command=root.destroy)
    btn_sair.pack(pady=20)

    root.mainloop()
