import requests

# Variável global para armazenar dados dos países
paises_data = []

def carregar_paises():
    global paises_data
    try:
        response = requests.get("https://restcountries.com/v3.1/all")
        response.raise_for_status()  # Verifica se a requisição foi bem-sucedida
        paises_data = response.json()  # Armazena o JSON de resposta na variável global
        print("Dados dos países carregados com sucesso.")
    except requests.RequestException as e:
        print(f"Erro ao carregar países: {e}")
        paises_data = []

def obter_pais_por_indice(indice):
    if 0 <= indice < len(paises_data):
        return paises_data[indice]['name']['common']
    else:
        return "Índice inválido"

def imprimir_json_com_espacos():
    for pais in paises_data:
        print(pais)
        print()  # Imprime uma linha em branco entre cada país

# Exemplo de uso:
carregar_paises()  # Carrega os dados
print(obter_pais_por_indice(0))  # Obtém o nome do primeiro país
imprimir_json_com_espacos()  # Imprime todos os países com uma linha em branco entre eles
