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


while True:
    qtd_notas = int(input('Qual a quatidade de notas? ')) #Definir a quantidade de vezes a solicitar a nota
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