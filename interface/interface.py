import customtkinter as ctk


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

        botao = ctk.CTkButton(janela, text="Depositar", command=confirmar_deposito)
        botao.pack(pady=10)

    btn_depositar = ctk.CTkButton(root, text="Depositar", command=acao_depositar)
    btn_depositar.pack(pady=5)

    btn_sacar = ctk.CTkButton(root, text="Sacar")
    btn_sacar.pack(pady=5)

    btn_saldo = ctk.CTkButton(root, text="Saldo")
    btn_saldo.pack(pady=5)

    btn_extrato = ctk.CTkButton(root, text="Extrato")
    btn_extrato.pack(pady=5)

    btn_exportar = ctk.CTkButton(root, text="Exportar Extrato")
    btn_exportar.pack(pady=5)

    btn_sair = ctk.CTkButton(root, text="Sair", command=root.destroy)
    btn_sair.pack(pady=20)

    root.mainloop()
