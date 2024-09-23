#import OS

def mostrar_menu():
    print("\nMenu")
    print("1. Adicionar Livro")
    print("2. Consultar Catálago")
    print("3. Excluir Livro")
    print("4. Sair")

def Ler_catalogo(Tabela):
    try:
        with open(Tabela, 'r', encoding='utf-8') as arquivo:
            livros = arquivo.readlines()
            return [livro.strip() for livro in livros]
    except FileNotFoundError:
            return[]

def adicionar_livro(Tabela):
    titulo = input("Digite o titulo do livro: ")
    autor = input("Digite o autor do livro: ")
    with open(Tabela, 'a', encoding='utf-8') as arquivos:
        arquivos.write(f"{titulo} - {autor}\n")
    print(f"Livro '{titulo}' de {autor} adicionado ao catálago.")

def Consultar_catalago(Tabela):
    livros = Ler_catalogo(Tabela)
    if livros:
        print("\nCatálago de livros:")
        for livro in livros:
            print(livro)
        else:
            print("O catálago está vazio.")
            
def excluir_livro(Tabela):
    livros = Ler_catalogo(Tabela)
    if livros:
        print("\nCAtálago de Livros:")
        for i, livro in enumerate(livros, 1):
            print(f"{i}, {livro}")
            escolha = int(input("Digite o número do livroo que deseja excluir:  "))
            if 1 <= escolha <= len(livro):
                livro_excluido = livros.pop(escolha - 1)
                with open (Tabela, 'w', encoding='utf-8') as arquivo:
                    for livro in livros:
                        arquivo.write(f"{livro}\n")
                    print(f"Livro'{livro_excluido}'excluído do catálago.")
            else:
                print("O catálago está vazio.")

def Menu_case(Tabela):
    while True:
        mostrar_menu()
        try:
            Num = int(input("Escolha uma opção: "))
            if Num == 1:
                adicionar_livro(Tabela)
            elif Num == 2:
                Consultar_catalago(Tabela)
            elif Num == 3:
                excluir_livro(Tabela)
            elif Num == 4:
                print("Saindo do programa...")
                break
            else:
                print(f"Opção {Num} inválida.")
        except ValueError:
            print("Por favor, digite um número válido.")

Tabela = "Tabela.txt"
Menu_case(Tabela)
