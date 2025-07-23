import pandas as pd
import re

def transform_characters(raw_characters):
    """
    Transforma a lista de personagens em um DataFrame com colunas normalizadas:
    nome, status, espécie, gênero, origem, localização e número de episódios.
    """
    df = []
    
    for personagem in raw_characters:
        df.append({
            'id': personagem['id'],
            'nome': personagem['name'],
            'status': personagem['status'],
            'especie': personagem['species'],
            'genero':personagem['gender'],
            'origem': personagem['origin']['name'],
            'localizacao':personagem['location']['name'],
            'episodios': len(personagem['episode'])
        })
    
    data = pd.DataFrame(df)
    #print(f'Personagens: \n{data.head(3)}')
    return data

def transform_episodes(raw_episodes):
    '''
    Transforma a lista de episodios em um DataFrame com colunas normalizadas:
    nome, data_de_exibicao, temporada_episodio, personagens_envolvidos.
    '''
    df = []

    for e in raw_episodes:

       # Filtrando Ids dos personagens
       ids = [int(re.search(r'/character/(\d+)', url).group(1)) for url in e['characters']]

       df.append({
            'nome': e['name'],
            'data_de_exibicao': e['air_date'],
            'temporada_episodio': e['episode'],
            'personagens_envolvidos': ids
        })
   
    data = pd.DataFrame(df)
    data[['Temporada', 'Episodio']] = data['info'].str.extract(r'S(\d+)E(\d+)').astype(int)
    return data
   
   
       
def transform_locations(raw_locations):
   '''
   Transforma a lista de episodios em um DataFrame com colunas normalizadas:
    nome, tipo, dimensão, número de residentes.
   '''
   df = []

   for l in raw_locations:
       df.append({
            'nome': l['name'],
            'tipo': l['type'],
            'dimensao': l['dimension'], 
            'residentes': len(l['residents'])
        })
       
   data = pd.DataFrame(df)
   return data
   