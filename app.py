# A biblioteca 'requests' permite que você envie solicitações HTTP em Python de maneira simples
import requests
# A biblioteca 'uuid' é usada para gerar um ID universal, usei para quando criar equipe
import uuid


def get_pokemon_info(pokemon):
    # Converte o nome do Pokémon para minúsculas, evitando erro quando consome api
    pokemon = pokemon.lower()
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'  # URL da API
    response = requests.get(url)  # Faz uma solicitação GET para a API

    # Verifica se a resposta foi bem-sucedida e vê se volta algo
    if response.status_code == 200 and response.text.strip():
        data = response.json()  # Converte a resposta em JSON
        # Retorna um dicionário com as informações do Pokémon, solicitados no desafio
        return {
            'id': data["id"],
            'name': data["name"],
            'weight': data["weight"],
            'height': data["height"]
        }
    else:
        print(
            f'Não encontramos o Pokémon {pokemon}. Por favor, verifique se você digitou o nome corretamente. Lembre-se de que o nome do Pokémon deve estar em inglês!\n')
        return None
# caso não encontre nada, vai pergunta novamente com um texto alertando o usuario


# Função para criar uma equipe de Pokémon:
def create_pokemon_team():
    team = []  # Lista para armazenar a equipe de Pokémon
    while True:
        # Solicita ao usuário o nome de um Pokémon para adicionar à equipe
        pokemon = input(
            'Digite o nome do Pokémon para adicionar na pokebola|(ou "sair" para ver todos pokemons adicionados): ')
        if pokemon.lower() == 'sair':  # sair para criar uma equipe ou para não criar nenhuma equipe caso não tenha adicionado nada
            break
        elif pokemon.strip() == '':
            # caso o usuario dê enter  sem digitar nada
            print('Você não digitou nada. Digite o nome de algum pokemon.')
            continue
        # Obtém as informações do Pokémon
        pokemon_info = get_pokemon_info(pokemon)
        if pokemon_info:
            team.append(pokemon_info)  # Adiciona o Pokémon à equipe
            # Imprime as informações do Pokémon solicitadas no desafio
            print(
                f'ID: {pokemon_info["id"]}, Nome: {pokemon_info["name"]}, Peso: {pokemon_info["weight"]}, Altura: {pokemon_info["height"]}\n')

    # Solicita ao usuário o nome para criar a equipe,
    team_name = input('Qual nome você quer para a equipe? ')
    team_id = str(uuid.uuid4())  # Gera um ID único para a equipe
    print(
        f'\nTime de Pokémon {team_name} criado com sucesso! ID da equipe: {team_id}\n')

    # Escreve as informações do time de Pokémon em um arquivo de texto
    with open(f'{team_name}_{team_id}.txt', 'w') as f:
        # Escreve o nome e o ID da equipe no arquivo
        f.write(f'Time: {team_name}, ID da equipe: {team_id}\n')
        # Para cada Pokémon na equipe, escreve suas informações no arquivo
        for pokemon in team:
            f.write(
                f'ID: {pokemon["id"]}, Nome: {pokemon["name"]}, Peso: {pokemon["weight"]}, Altura: {pokemon["height"]}\n')


# Chama a função para criar uma equipe de Pokémon
create_pokemon_team()
