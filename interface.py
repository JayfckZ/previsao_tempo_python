import tkinter as tk
from tkinter import ttk
from previsao import buscar_previsao_atual
from analise import analisa_dia


def mostrar_previsao():
    cidade = entry_cidade.get()
    dia_atual = buscar_previsao_atual(cidade)
    proximos_dias = analisa_dia(cidade)

    res_final = dia_atual + "\n\n"
    if proximos_dias:
        for dia in proximos_dias:
            res_final += dia + "\n\n"
        label_result.config(text=res_final)
    else:
        label_result.config(text="Erro ao obter a previsão.")


janela = tk.Tk()
janela.title("Previsão do Tempo")
janela.geometry("1024x900")
janela.config(bg="#87CEEB")

label_titulo = ttk.Label(
    janela,
    text="Digite o nome da cidade:",
    background="#87CEEB",
    foreground="white",
    font=("Arial", 16),
)
label_titulo.pack(pady=10)

entry_cidade = ttk.Entry(janela)
entry_cidade.pack(pady=10)

style = ttk.Style()
style.configure("TButton", background="white", foreground="black")

btn_obter_previsao = ttk.Button(
    janela, text="Obter Previsão", command=mostrar_previsao, style="TButton"
)
btn_obter_previsao.pack(pady=20)

label_result = ttk.Label(
    janela,
    text="",
    background="#87CEEB",
    foreground="white",
    font=("Arial", 14),
    justify="center",
    wraplength=350,
)
label_result.pack(pady=20)

janela.mainloop()
