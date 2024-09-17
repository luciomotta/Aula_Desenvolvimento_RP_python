import tkinter as tk # pip instal tkinter
from tkinter import ttk
import requests  # Importa a biblioteca requests para fazer requisições HTTP pip install requests

#APi de PAíses
def carregar_paises():
    try:
        response = requests.get("https://restcountries.com/v3.1/all")
        response.raise_for_status()  # Verifica se a requisição foi bem-sucedida
        data = response.json()
        paises = [pais['name']['common'] for pais in data]
        combo_pais['values'] = paises
    except requests.RequestException as e:
        print(f"Erro ao carregar países: {e}")
        combo_pais['values'] = ["Erro ao carregar países"]

def sair():
    root.destroy()

# Criando janela "
root = tk.Tk()
root.title("Aula03")

#cRIANDO menu
menu = tk.Menu(root)
root.config(menu=menu)
subMenu = tk.Menu(menu)
menu.add_cascade(label="Opções", menu=subMenu)
subMenu.add_command(label="Sair", command=root.quit)

#campo de formulario
tk.Label(root, text="Nome").grid(row=0, column=0, padx=10, pady=10)
entry_nome = tk.Entry(root)
entry_nome.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Idade").grid(row=1, column=0, padx=10, pady=10)
entry_idade = tk.Entry(root)
entry_idade.grid(row=1, column=1, padx=10, pady=10)

#Radio button
tk.Label(root, text="Gênero: ").grid(row=2, column=0, padx= 10, pady=10)
genero_var = tk.StringVar()
tk.Radiobutton(root, text="Masculino", variable=genero_var, value=1).grid(row=2, column=1, padx=10, pady=12)
tk.Radiobutton(root, text="Feminino", variable=genero_var, value=2).grid(row=2, column=2, padx=10, pady=12)

#CheckList
tk.Label(root, text="Interesses:").grid(row=3, column=0, padx=10, pady=10)
var_python = tk.BooleanVar()
tk.Checkbutton(root, text="Python", variable=var_python).grid(row=3, column=1, padx=10, pady=10)
var_java= tk.BooleanVar()
tk.Checkbutton(root, text="Java", variable=var_java).grid(row=3, column=2, padx=10, pady=10)
var_js = tk.BooleanVar()
tk.Checkbutton(root, text="JavaScript", variable=var_js).grid(row=3, column=3, padx=10, pady=10)

#CAixa de combinação
tk.Label(root, text="País:").grid(row=4, column=0, padx=10, pady=10)
combo_pais = ttk.Combobox(root)
combo_pais.grid(row=4, column=1, padx=10, pady=10)
carregar_paises()

# Botão de comando
tk.Button(root, text="SAir", command=sair). grid(row=5, column=1, padx=10, pady=10)


#inicar o LOOOP
root.mainloop()