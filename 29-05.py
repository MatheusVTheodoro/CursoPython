import pandas as pd
import os
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

# Nome do arquivo Excel
FILENAME = 'clientes.xlsx'

# Verifica se o arquivo Excel já existe, caso contrário cria um novo
if not os.path.exists(FILENAME):
    df = pd.DataFrame(columns=['Nome', 'Telefone', 'Status'])
    df.to_excel(FILENAME, index=False)

def listar_clientes():
    df = pd.read_excel(FILENAME)
    return df

def adicionar_cliente(nome, telefone, status='Novo Cliente'):
    df = pd.read_excel(FILENAME)
    novo_cliente = pd.DataFrame({'Nome': [nome], 'Telefone': [telefone], 'Status': [status]})
    df = pd.concat([df, novo_cliente], ignore_index=True)
    df.to_excel(FILENAME, index=False)

def editar_cliente(indice, nome, telefone, status):
    df = pd.read_excel(FILENAME)
    if indice < 0 or indice >= len(df):
        return False
    else:
        df.at[indice, 'Nome'] = nome
        df.at[indice, 'Telefone'] = telefone
        df.at[indice, 'Status'] = status
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

        self.kanban_frame = tk.Frame(self.root)
        self.kanban_frame.pack(pady=10)

        self.statuses = ['Novo Cliente', 'Em Processo', 'Concluído']
        self.listas = {}

        for status in self.statuses:
            frame = tk.Frame(self.kanban_frame)
            frame.pack(side=tk.LEFT, padx=10)
            label = tk.Label(frame, text=status)
            label.pack()
            listbox = tk.Listbox(frame, selectmode=tk.SINGLE)
            listbox.pack()
            self.listas[status] = listbox

        self.btn_editar = tk.Button(self.root, text="Editar Cliente", command=self.editar_cliente)
        self.btn_editar.pack(pady=5)

        self.btn_deletar = tk.Button(self.root, text="Deletar Cliente", command=self.deletar_cliente)
        self.btn_deletar.pack(pady=5)

        self.atualizar_kanban()

    def atualizar_kanban(self):
        for status in self.statuses:
            self.listas[status].delete(0, tk.END)
        
        df = listar_clientes()
        for idx, row in df.iterrows():
            self.listas[row['Status']].insert(tk.END, f"{idx}: {row['Nome']} - {row['Telefone']}")

    def adicionar_cliente(self):
        nome = self.entry_nome.get()
        telefone = self.entry_telefone.get()
        if nome and telefone:
            adicionar_cliente(nome, telefone)
            self.entry_nome.delete(0, tk.END)
            self.entry_telefone.delete(0, tk.END)
            self.atualizar_kanban()
        else:
            messagebox.showerror("Erro", "Nome e telefone são obrigatórios")

    def editar_cliente(self):
        status_idx_map = {}
        for status in self.statuses:
            selected = self.listas[status].curselection()
            if selected:
                status_idx_map[status] = int(selected[0])
                break

        if not status_idx_map:
            messagebox.showerror("Erro", "Nenhum cliente selecionado")
            return

        status = list(status_idx_map.keys())[0]
        indice = status_idx_map[status]
        nome = simpledialog.askstring("Editar Cliente", "Novo Nome:", initialvalue=self.listas[status].get(indice).split(': ')[1].split(' - ')[0])
        telefone = simpledialog.askstring("Editar Cliente", "Novo Telefone:", initialvalue=self.listas[status].get(indice).split(': ')[1].split(' - ')[1])
        novo_status = simpledialog.askstring("Editar Cliente", "Novo Status:", initialvalue=status)

        if nome and telefone and novo_status:
            if editar_cliente(indice, nome, telefone, novo_status):
                self.atualizar_kanban()
            else:
                messagebox.showerror("Erro", "Índice inválido")
        else:
            messagebox.showerror("Erro", "Nome, telefone e status são obrigatórios")

    def deletar_cliente(self):
        status_idx_map = {}
        for status in self.statuses:
            selected = self.listas[status].curselection()
            if selected:
                status_idx_map[status] = int(selected[0])
                break

        if not status_idx_map:
            messagebox.showerror("Erro", "Nenhum cliente selecionado")
            return

        status = list(status_idx_map.keys())[0]
        indice = status_idx_map[status]

        if deletar_cliente(indice):
            self.atualizar_kanban()
        else:
            messagebox.showerror("Erro", "Índice inválido")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
