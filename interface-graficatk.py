import tkinter as tk

# Função para alternar entre as páginas
def mostrar_pagina(pagina):
    pagina1.pack_forget()
    pagina2.pack_forget()
    pagina.pack(fill="both", expand=True)

# Função para mostrar/esconder o menu
def toggle_menu():
    if menu_frame.winfo_ismapped():
        menu_frame.pack_forget()
    else:
        menu_frame.pack(side="left", fill="y")

# Janela principal
janela = tk.Tk()
janela.title("Telas")
janela.geometry("900x600")
janela.configure(bg="black")

# Menu hambúrguer (botão lateral)
botao_menu = tk.Button(
    janela,
    text="☰",  # Ícone hambúrguer
    command=toggle_menu,
    bg="white",
    fg="black",
    font=("Arial", 16, "bold")
)
botao_menu.pack(anchor="nw", padx=10, pady=10)

# Frame do menu lateral
menu_frame = tk.Frame(janela, bg="gray20", width=200)

botao_pagina1 = tk.Button(menu_frame, text="Página 1", command=lambda: mostrar_pagina(pagina1), bg="white")
botao_pagina2 = tk.Button(menu_frame, text="Página 2", command=lambda: mostrar_pagina(pagina2), bg="white")

botao_pagina1.pack(pady=10, fill="x")
botao_pagina2.pack(pady=10, fill="x")

# Página 1
pagina1 = tk.Frame(janela, bg="black")
tk.Label(pagina1, text="Esta é a Página 1", font=("Arial", 18), fg="white", bg="black").pack(pady=50)

# Página 2
pagina2 = tk.Frame(janela, bg="darkblue")
tk.Label(pagina2, text="Esta é a Página 2", font=("Arial", 18), fg="white", bg="darkblue").pack(pady=50)

# Mostra a primeira página ao iniciar
mostrar_pagina(pagina1)

# Loop principal
janela.mainloop()
