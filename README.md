# Sistema de Controle Financeiro 

![Demonstração do Sistema](https://github.com/user-attachments/assets/efc4adcf-fbd3-4c70-a2e3-56cbfaff3d42)

## Objetivo
Aplicativo desktop estruturado para controle financeiro, focado no gerenciamento de contas empresariais com persistência de dados local.

## Decisões de Arquitetura
* **Programação Orientada a Objetos (POO):** O sistema utiliza classes e objetos para modelar as regras de negócio de forma modular, garantindo um código limpo e de fácil manutenção.
* **Separação de Responsabilidades (MVC):** O projeto está dividido em camadas claras, isolando as regras de negócio (`metodos`), a persistência de dados (`banco_dados`) e a interação visual (`interface`).

## Stack Tecnológica
* **Motor Principal:** Python
* **Interface (UI/UX):** CustomTkinter (junto à biblioteca `rich` para formatação em terminal)
* **Banco de Dados:** SQLite nativo

## Guia de Execução

1. Certifique-se de ter o Python instalado na sua máquina.
2. Instale as dependências necessárias executando o comando abaixo no terminal do seu projeto:
   ```bash
   pip install customtkinter rich
