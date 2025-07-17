import pandas as pd

def transform_characters(row_characters):
    characters = row_characters
    df = []
    
    for personagem in characters:
        # Personagens: nome, status, espécie, gênero, origem, localização atual, episódios
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

def transform_episodes(row_episodes):
   episodes  = row_episodes
   df = []

   for e in episodes:
       # Episódios: nome, data de exibição, personagens envolvidos
       df.append({
            'nome': e['name'],
            'data_de_exibicao': e['air_date'],
            'info': e['episode'],
            'personagens_envolvidos': e['characters']
        })
       
   data = pd.DataFrame(df)
   return data
   
   
       
def transform_locations(row_locations):
   locations  = row_locations
   df = []
   
   for l in locations:
       # Localizações: nome, tipo, dimensão, número de residentes
       df.append({
            'nome': l['name'],
            'tipo': l['type'],
            'dimensao': l['dimension'], 
            'residentes': len(l['residents'])
        })
       
   data = pd.DataFrame(df)
   return data
       

   
   