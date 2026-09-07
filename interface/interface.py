# Import do customtkinter para configurar o deskotp.
import customtkinter as ctk
from metodos.fintech import ContaBancaria
from controle.controlador import ControladorFinanceiro


# Coloquei uma mensagem de erro mundial pro codigo não ficar poluído.
def mensagem_erro(mensagem):
    janela_erro = ctk.CTkToplevel()
    janela_erro.title("Erro")
    janela_erro.geometry("250x150")

    label = ctk.CTkLabel(janela_erro, text=mensagem)
    label.pack(pady=20)

    botao = ctk.CTkButton(janela_erro, text="OK", command=janela_erro.destroy)
    botao.pack(pady=10)


# Aqui é aonde inicia a interface, busco o cb e cb_repo do main e do banco.
def iniciar_interface(controlador):
    # Root mexe na tela principal.
    root = ctk.CTk()

    root.title("Sistema Fintech")
    root.geometry("500x500")

    titulo = ctk.CTkLabel(root, text="Sistema Fintech", font=("Arial", 28, "bold"))
    titulo.pack(pady=30)

    lbl_saldo = ctk.CTkLabel(
        root, text=controlador.obter_saldo_inicial(), font=("Arial", 12, "bold")
    )
    lbl_saldo.pack()

    def acao_depositar():
        # ctk.CTkToplevel() cria pop-ups.
        janela = ctk.CTkToplevel()
        janela.title("Depositar")
        janela.geometry("300x200")

        label = ctk.CTkLabel(janela, text="Digite o valor do depósito:")
        label.pack(pady=20)

        entrada = ctk.CTkEntry(janela, placeholder_text="Ex: 100.00")
        entrada.pack(pady=10)

        def confirmar_deposito():
            valor = entrada.get()
            sucesso, mensagem = controlador.processar_deposito(valor)
            lbl_saldo.configure(text=mensagem)
            if sucesso:
                janela.destroy()
            else:
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
            sucesso, mensagem = controlador.processar_saque(valor)
            lbl_saldo.configure(text=mensagem)
            if sucesso:
                janela.destroy()
            else:
                entrada.delete(0, "end")

        # Função para fazer os botões clicaveis.
        botao = ctk.CTkButton(janela, text="Sacar", command=confirmar_saque)
        botao.pack(pady=20)

    def acao_extrato():
        janela = ctk.CTkToplevel()
        janela.title("Extrato da conta")
        janela.geometry("400x400")

        exibicao_texto = ctk.CTkTextbox(janela, width=350, height=300)
        exibicao_texto.pack(pady=20)

        movimentos = controlador.obter_extrato()
        for movimento in movimentos:
            exibicao_texto.insert("end", movimento + "\n")

        botao = ctk.CTkButton(janela, text="Fechar", command=janela.destroy)
        botao.pack(pady=20)

    def acao_exportar():
        janela = ctk.CTkToplevel()
        janela.title("Extrato")
        janela.geometry("250x150")

        sucesso, mensagem = controlador.processar_exportacao()
        label = ctk.CTkLabel(janela, text=mensagem)
        label.pack(pady=20)

        botao = ctk.CTkButton(janela, text="Ok", command=janela.destroy)
        botao.pack(pady=20)

    # Função que cria os botões.
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
