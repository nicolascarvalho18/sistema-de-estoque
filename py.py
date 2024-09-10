import tkinter as tk
from tkinter import messagebox
import csv


estoque = {}

def carregar_estoque(arquivo_csv):
    global estoque
    with open(arquivo_csv, mode='r') as file:
        reader = csv.reader(file)
        for linha in reader:
            codigo_barras, nome, quantidade = linha
            estoque[codigo_barras] = {'nome': nome, 'quantidade': int(quantidade)}


def exibir_estoque():
    lista_estoque.delete(0, tk.END)
    for codigo, info in estoque.items():
        lista_estoque.insert(tk.END, f"{codigo} | {info['nome']} | {info['quantidade']}")


def adicionar_produto():
    codigo_barras = entrada_codigo.get()
    quantidade = int(entrada_quantidade.get())
    if codigo_barras in estoque:
        estoque[codigo_barras]['quantidade'] += quantidade
    else:
        messagebox.showerror("Erro", "Produto não encontrado no estoque.")
    exibir_estoque()

def remover_produto():
    codigo_barras = entrada_codigo.get()
    quantidade = int(entrada_quantidade.get())
    if codigo_barras in estoque:
        if estoque[codigo_barras]['quantidade'] >= quantidade:
            estoque[codigo_barras]['quantidade'] -= quantidade
        else:
            messagebox.showerror("Erro", "Quantidade insuficiente no estoque.")
    else:
        messagebox.showerror("Erro", "Produto não encontrado no estoque.")
    exibir_estoque()

root = tk.Tk()
root.title("Sistema de Estoque")


carregar_estoque('estoque.csv')

tk.Label(root, text="Código de Barras").grid(row=0, column=0)
entrada_codigo = tk.Entry(root)
entrada_codigo.grid(row=0, column=1)

tk.Label(root, text="Quantidade").grid(row=1, column=0)
entrada_quantidade = tk.Entry(root)
entrada_quantidade.grid(row=1, column=1)


tk.Button(root, text="Adicionar Produto", command=adicionar_produto).grid(row=2, column=0, columnspan=2, pady=5)
tk.Button(root, text="Remover Produto", command=remover_produto).grid(row=3, column=0, columnspan=2, pady=5)


tk.Label(root, text="Estoque Atual").grid(row=4, column=0, columnspan=2)
lista_estoque = tk.Listbox(root, width=50)
lista_estoque.grid(row=5, column=0, columnspan=2, pady=10)


exibir_estoque()

root.mainloop()
