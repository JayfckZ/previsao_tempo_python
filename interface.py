import tkinter as tk
from tkinter import messagebox
from previsao import obter_previsao

def mostrar_previsao():
    cidade = entry_cidade.get()
    if cidade:
        resultado = obter_previsao(cidade)
        messagebox.showinfo("PRevisão do Tempo", resultado)
    else:
        messagebox.showerror("Erro", "Por favor, insira o nome da cidade.")

janela = tk.Tk()
janela.title("Previsão do Tempo")
janela.geometry("300x150")

label_titulo = tk.Label(janela, text="Digite o nome da cidade:")
label_titulo.pack(pady=10)

entry_cidade = tk.Entry(janela)
entry_cidade.pack(pady=5)

btn_obter_previsao = tk.Button(janela, text="Obter Previsão", command=mostrar_previsao)
btn_obter_previsao.pack(pady=10)

janela.mainloop()