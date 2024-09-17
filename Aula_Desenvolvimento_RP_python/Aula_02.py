def Media_Notas(notas):
    # Calcula a soma e a média das notas
    soma = sum(notas)
    media = soma / len(notas)
    return media

def obter_notas(qtd_notas):
    notas = []
    for i in range(qtd_notas):
        while True:
            try:
                #SOlicitar a NOta do USER
                nota = float(input(f'Digite a {1 + i}º nota: '))
                notas.append(nota)
                break
            except VAlueError:
                print('Por favor, insira um valor numerico válido.')
    return notas

def tabuada(num):

    for i in range (1, 11):
        print(f"{num} x {i} = {num*i}")
        
def ordem():
    Order = [5,6,7,8,10,65,3,1,6,9,5]
    
    produto = [
        {'nome': 'chocolate', 'valor': 3.45},
        {'nome': 'biscoito', 'valor': 2.49},
        {'nome': 'cafe', 'valor': 3.45},
        {'nome': 'suco', 'valor': 4.3},
        {'nome': 'feijao', 'valor': 10.0},
        {'nome': 'arroz', 'valor': 8.5}
    ]
                    
    result_ordenado = sorted(Order, reverse=False)
    

    
    print(f"Agora a lista ordenada pelo SORTED({result_ordenado})")
    
    """result_prod_nome = sorted(produto, key=produto.nome)"""
    
    #Ordenar  a lista de números
    result_prod_nome = sorted(produto, key=lambda x: x['nome'])
    print(f"Lista de produto ordenado por nome: {result_prod_nome}")
    for p in result_prod_nome:
        print(f"Nome: {p['nome']}, valor: {p['valor']}")
  
    """
        # Ordena a lista produto pelo nome dos produtos
    result_prod_nome = sorted(produto, key=lambda x: x['nome'])
    print('Lista de produtos ordenada por nome:')
    for p in result_prod_nome:
        print(f"Nome: {p['nome']}, Valor: {p['valor']}")
    """
    

        
while True: 

    print('\nEscolha uma opção:')
    print('1. Calcular a média das notas')
    print('2. Ver a tabuada de um número')
    print('3. Lista de Produtos')
    print('4. Sair')

    try:
        result = int(input('Digite a opção desejada (1/2/3/4): '))
    except ValueError:
        print('Entrada inválida. Por favor, insira um número.')
        continue
    
    if result == 1:
    
        qtd_notas = int(input('Qual a quatidade de notas? ')) 
        #Definir a quantidade de vezes a solicitar a nota
        
        notas = obter_notas(qtd_notas)
        
        resultado = Media_Notas(notas)
        print(f'A média das notas é: {resultado}')
          # Encontra a maior nota
        maior_nota = max(notas)
        if resultado >= 7:
            print(f'SUa nota esta na media, a maior foi {maior_nota}')
        else:
            print('EStude MAIs!!!!')
      # Pergunta ao usuário se deseja continuar
        continuar = input('Deseja inserir novas notas? (s/n): ')
        if continuar.lower() != 's':
            break
    
    elif result == 2:
        #tabuada(int(input('Digite um Nº e veja atabuada: '))
        tabuada(int(input('Digite um número para ver a tabuada: ')))
    elif result == 3:
        ordem()
        
    else:
        break
    
    