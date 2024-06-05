import tkinter as tk
from tkinter import messagebox

# Funções de operações
def click(event):
    global expression
    expression += event.widget.cget("text")
    input_text.set(expression)

def clear():
    global expression
    expression = ""
    input_text.set("")

def evaluate():
    global expression
    try:
        result = str(eval(expression))
        input_text.set(result)
        expression = result
    except:
        input_text.set("Erro")
        expression = ""

# Configuração da janela principal
root = tk.Tk()
root.title("Calculadora")

expression = ""
input_text = tk.StringVar()

# Frame de entrada
input_frame = tk.Frame(root)
input_frame.pack()

input_field = tk.Entry(input_frame, textvar=input_text, font=('arial', 18, 'bold'), bd=10, insertwidth=2, width=14, borderwidth=4)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)

# Frame dos botões
btns_frame = tk.Frame(root)
btns_frame.pack()

# Primeira linha
btns = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['C', '0', '=', '+']
]

for i in range(4):
    for j in range(4):
        btn = tk.Button(btns_frame, text=btns[i][j], font=('arial', 18, 'bold'), fg="black", width=7, height=2, bd=1, relief="raised")
        btn.grid(row=i, column=j)
        if btns[i][j] == 'C':
            btn.config(command=clear)
        elif btns[i][j] == '=':
            btn.config(command=evaluate)
        else:
            btn.bind('<Button-1>', click)

# Inicia a aplicação
root.mainloop()
