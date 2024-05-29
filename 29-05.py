import pandas as pd
import os

# Nome do arquivo Excel
FILENAME = 'clientes.xlsx'

# Verifica se o arquivo Excel já existe, caso contrário cria um novo
if not os.path.exists(FILENAME):
    df = pd.DataFrame(columns=['Nome', 'Telefone'])
    df.to_excel(FILENAME, index=False)

def listar_clientes():
    df = pd.read_excel(FILENAME)
    if df.empty:
        print("Nenhum cliente cadastrado.")
    else:
        print(df)

def adicionar_cliente(nome, telefone):
    df = pd.read_excel(FILENAME)
    novo_cliente = pd.DataFrame({'Nome': [nome], 'Telefone': [telefone]})
    df = pd.concat([df, novo_cliente], ignore_index=True)
    df.to_excel(FILENAME, index=False)
    print(f"Cliente {nome} adicionado com sucesso!")

def editar_cliente(indice, nome, telefone):
    df = pd.read_excel(FILENAME)
    if indice < 0 or indice >= len(df):
        print("Índice inválido.")
    else:
        df.at[indice, 'Nome'] = nome
        df.at[indice, 'Telefone'] = telefone
        df.to_excel(FILENAME, index=False)
        print(f"Cliente no índice {indice} atualizado com sucesso!")

def deletar_cliente(indice):
    df = pd.read_excel(FILENAME)
    if indice < 0 or indice >= len(df):
        print("Índice inválido.")
    else:
        df = df.drop(index=indice)
        df.to_excel(FILENAME, index=False)
        print(f"Cliente no índice {indice} deletado com sucesso!")

def menu():
    while True:
        print("\nMenu:")
        print("1. Listar clientes")
        print("2. Adicionar cliente")
        print("3. Editar cliente")
        print("4. Deletar cliente")
        print("5. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            listar_clientes()
        elif escolha == '2':
            nome = input("Nome do cliente: ")
            telefone = input("Telefone do cliente: ")
            adicionar_cliente(nome, telefone)
        elif escolha == '3':
            listar_clientes()
            indice = int(input("Índice do cliente a ser editado: "))
            nome = input("Novo nome do cliente: ")
            telefone = input("Novo telefone do cliente: ")
            editar_cliente(indice, nome, telefone)
        elif escolha == '4':
            listar_clientes()
            indice = int(input("Índice do cliente a ser deletado: "))
            deletar_cliente(indice)
        elif escolha == '5':
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
