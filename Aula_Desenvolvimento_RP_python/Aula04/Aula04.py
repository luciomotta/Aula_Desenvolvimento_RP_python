import os

# Verificar diretório de trabalho
print("Diretório de trabalho atual:", os.getcwd())

def  pegarLinhas(nome_arq):
        # Testando read()
    print("Usando read():")
    with open(nome_arq, "r", encoding="UTF-8") as arquivo:
        conteudo = arquivo.read()
        print(conteudo)
    print("\n" + "-"*40 + "\n")

    # Testando readline()
    print("Usando readline():")
    with open(nome_arq, "r", encoding="utf-8") as arquivo:
        linha = arquivo.readline()
        while linha:
            print(linha, end='')  # end='' para evitar adicionar uma nova linha extra
            linha = arquivo.readline()
    print("\n" + "-"*40 + "\n")

    # Testando readlines()
    print("Usando readlines():")
    with open(nome_arq, "r", encoding="UTF-8") as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas:
            print(linha, end='')  # end='' para evitar adicionar uma nova linha extra




# Abrir o arquivo
try:
    nome_arq = "Aula04/test.txt"
    arquivo = open(nome_arq, "r")
    # Fazer algo com o arquivo
    #conteudo = arquivo.read()
    #print(conteudo)
    print('Arquivo NOME:', arquivo.name) # Pegar o nome do arquivo
    print('Arquivo MODE:', arquivo.mode) # estado do arquivo (R, A, U, )
    print('Arquivo foi Fechado', arquivo.closed, '\n') # FALSE


    pegarLinhas(nome_arq)
    arquivo.close()
    print('Arquivo foi Fechado', arquivo.closed) # True
except FileNotFoundError:
    print("O arquivo 'test.txt' não foi encontrado.")
