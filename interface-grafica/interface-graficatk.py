from tkinter import *
import tkinter as tk

# Define a função que será executada ao clicar no botão
def acao_personalizada():
    print("Botão personalizado clicado!")
    

# 1. Cria a janela principal apenas UMA vez.
janela = tk.Tk()
janela.title("home")



# 2. Cria o botão e o associa à janela criada acima
botao = tk.Button(
    janela,
    text="ligar",
    command=acao_personalizada,
    fg="black",                 # Cor do texto
    bg="white",                  # Cor de fundo
    font=("Arial", 12, "bold"), # Fonte e tamanho
    width=15,                   # Largura (em caracteres)
    height=2                    # Altura (em linhas de texto)
)


botao1 = tk.Button(
    janela,
    text="Personalizar",
    command=acao_personalizada,
    fg="black",                 # Cor do texto
    bg="white",                  # Cor de fundo
    font=("Arial", 12, "bold"), # Fonte e tamanho
    width=15,                   # Largura (em caracteres)
    height=2                    # Altura (em linhas de texto)
)

# 3. Posiciona o botão na janela
botao.pack(pady=20, padx=20)
botao1.pack(pady=21,padx=21)

# 4. Inicia o loop principal da aplicação apenas UMA vez, no final.
#no tkinter o mainloop e responsavel por iniciar a interfaçe grafica e deve ser colocada no final do programa poque inicia e 
#e faz que seja executado em loop
janela.mainloop()
