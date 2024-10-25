#.venv/import pandas as pd
import matplotlib.pyplot as plt
# pip install matplotlib
    # Abrir arquivo EXCEL
tabela = pd.read_excel(r"D:\Usuarios\05693833151\OneDrive - Senado Federal\Área de Trabalho\GitHub\Aula_Desenvolvimento_RP_python\Aula05\vendas.xlsx")


def consultas_tabela():

    print(tabela)

    # Calculando o valor da fatura
    faturamento = tabela["PrecoUnitario"].sum()

    # Faturamento total
    faturamento_formatado = f"{faturamento:,.2f}"
    print(f'Faturamento total R${faturamento_formatado}')

    # Calcular o faturamento por loja
    lojas = tabela[["ID Loja", "PrecoUnitario"]].groupby("ID Loja").sum().reset_index()

    # Formatar o faturamento por loja
    lojas['PrecoUnitario'] = lojas['PrecoUnitario'].apply(lambda x: f"R${x:,.2f}")

    # Exibir o faturamento por loja formatado
    print('Faturamento por loja')
    print(lojas)

    # Calcular o faturamento por loja e por produto
    faturamento_produto = tabela.groupby(["ID Loja", "Produto"])["PrecoUnitario"].sum().reset_index()

    # Formatar o faturamento por loja e por produto
    faturamento_produto['PrecoUnitario'] = faturamento_produto['PrecoUnitario'].apply(lambda x: f"R${x:,.2f}")

    # Exibir o faturamento por loja e por produto
    print('Faturamento por loja e por produto')
    print(faturamento_produto)

def graficos_vendas():
    tabela['Data da Venda'] = pd.to_datetime(tabela['Data da Venda'], format='%d/%m/%Y')

    #Extraindo o ano de Data da venda
    tabela['Ano'] = tabela['Data da Venda'].dt.year

    #Calculando o faturamento por ano
    faturamento_ano = tabela.groupby('Ano')['PrecoUnitario'].sum().reset_index()
    faturamento_ano.columns = ['Ano', 'Faturamento']

    #Criando o gráfico de faturamento por ano
    plt.figure(figsize=(10, 6))
    plt.bar(faturamento_ano['Ano'], faturamento_ano['faturamento'], color='skyblue')
    plt.xlabel('ano')
    plt.ylabel('Faturamento (R$)')
    plt.title('Faturamento por ano')
    plt.xticks(faturamento_ano['Ano'])
    plt.grid(axis='y')

    #Salvando o gráfico
    #plt.savefig("grafico_faturamento_ano.png", dpi=300)
    plt.show()




def main():
    while True:
        print("\nMenu:")
        print("1. Consultas Tabela")
        print("2. Gráficos Vendas")
        print("3. Consultas Gráficos")
        print("5. Sair")
        
        choice = input("Escolha uma opção: ")
        
        if choice == '1':
            consultas_tabela()
        elif choice == '2':
            graficos_vendas()
        elif choice == '3':
            consultas_graficos()
        elif choice == '5':
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()