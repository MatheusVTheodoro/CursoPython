import pandas as pd
import os
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

# Nome do arquivo Excel
FILENAME = 'clientes.xlsx'

# Verifica se o arquivo Excel já existe, caso contrário cria um novo
if not os.path.exists(FILENAME):
    df = pd.DataFrame(columns=['Nome', 'Telefone'])
    df.to_excel(FILENAME, index=False)

def listar_clientes():
    df = pd.read_excel(FILENAME)
    return df

def adicionar_cliente(nome, telefone):
    df = pd.read_excel(FILENAME)
    novo_cliente = pd.DataFrame({'Nome': [nome], 'Telefone': [telefone]})
    df = pd.concat([df, novo_cliente], ignore_index=True)
    df.to_excel(FILENAME, index=False)

def editar_cliente(indice, nome, telefone):
    df = pd.read_excel(FILENAME)
    if indice < 0 or indice >= len(df):
        return False
    else:
        df.at[indice, 'Nome'] = nome
        df.at[indice, 'Telefone'] = telefone
        df.to_excel(FILENAME, index=False)
        return True

def deletar_cliente(indice):
    df = pd.read_excel(FILENAME)
    if indice < 0 or indice >= len(df):
        return False
    else:
        df = df.drop(index=indice)
        df.to_excel(FILENAME, index=False)
        return True

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Cadastro de Clientes")

        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10)

        self.label_nome = tk.Label(self.frame, text="Nome")
        self.label_nome.grid(row=0, column=0)

        self.entry_nome = tk.Entry(self.frame)
        self.entry_nome.grid(row=0, column=1)

        self.label_telefone = tk.Label(self.frame, text="Telefone")
        self.label_telefone.grid(row=1, column=0)

        self.entry_telefone = tk.Entry(self.frame)
        self.entry_telefone.grid(row=1, column=1)

        self.btn_adicionar = tk.Button(self.frame, text="Adicionar Cliente", command=self.adicionar_cliente)
        self.btn_adicionar.grid(row=2, columnspan=2, pady=10)

        self.lista_clientes = tk.Listbox(self.root)
        self.lista_clientes.pack(pady=10)

        self.btn_editar = tk.Button(self.root, text="Editar Cliente", command=self.editar_cliente)
        self.btn_editar.pack(pady=5)

        self.btn_deletar = tk.Button(self.root, text="Deletar Cliente", command=self.deletar_cliente)
        self.btn_deletar.pack(pady=5)

        self.atualizar_lista()

    def atualizar_lista(self):
        self.lista_clientes.delete(0, tk.END)
        df = listar_clientes()
        for idx, row in df.iterrows():
            self.lista_clientes.insert(tk.END, f"{idx}: {row['Nome']} - {row['Telefone']}")

    def adicionar_cliente(self):
        nome = self.entry_nome.get()
        telefone = self.entry_telefone.get()
        if nome and telefone:
            adicionar_cliente(nome, telefone)
            self.entry_nome.delete(0, tk.END)
            self.entry_telefone.delete(0, tk.END)
            self.atualizar_lista()
        else:
            messagebox.showerror("Erro", "Nome e telefone são obrigatórios")

    def editar_cliente(self):
        selected = self.lista_clientes.curselection()
        if selected:
            indice = int(selected[0])
            nome = simpledialog.askstring("Editar Cliente", "Novo Nome:", initialvalue=self.lista_clientes.get(selected).split(': ')[1].split(' - ')[0])
            telefone = simpledialog.askstring("Editar Cliente", "Novo Telefone:", initialvalue=self.lista_clientes.get(selected).split(': ')[1].split(' - ')[1])
            if nome and telefone:
                if editar_cliente(indice, nome, telefone):
                    self.atualizar_lista()
                else:
                    messagebox.showerror("Erro", "Índice inválido")
            else:
                messagebox.showerror("Erro", "Nome e telefone são obrigatórios")
        else:
            messagebox.showerror("Erro", "Nenhum cliente selecionado")

    def deletar_cliente(self):
        selected = self.lista_clientes.curselection()
        if selected:
            indice = int(selected[0])
            if deletar_cliente(indice):
                self.atualizar_lista()
            else:
                messagebox.showerror("Erro", "Índice inválido")
        else:
            messagebox.showerror("Erro", "Nenhum cliente selecionado")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
