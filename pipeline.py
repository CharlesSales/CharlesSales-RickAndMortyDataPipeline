from extract.extract import fetch_all_endpoints
from transform.transform import transform_locations, transform_characters, transform_episodes
from load.load import *
import os
from dotenv import load_dotenv

def run_pipeline():

    load_dotenv()
    
    # Carregar APIs
    characters_api = os.getenv('url_character') 
    locations_api = os.getenv('url_locations')
    episodes_api = os.getenv('url_episodes')
    db_key = os.getenv('db_key')

    print("Character API:", characters_api)

    # Carregar endpoints
    characters = fetch_all_endpoints(characters_api)
    locations = fetch_all_endpoints(locations_api)
    episodes = fetch_all_endpoints(episodes_api)

    # Tranformar os dados
    df_characters = transform_characters(characters)
    df_episodes = transform_episodes(episodes)
    df_locations = transform_locations(locations)

    # Salvar como parquet
    save_as_parquet(df_characters, 'characters')
    save_as_parquet(df_episodes, 'episodes')
    save_as_parquet(df_locations, 'locations')

    # Salvar no DB
    save_as_db(db_key, df_characters, 'personagens')
    save_as_db(db_key, df_episodes, 'episodios')
    save_as_db(db_key, df_locations, 'localizacao')

    # Salvar como csv
    save_as_csv(df_characters, 'characters')
    save_as_csv(df_episodes, 'episodes')
    save_as_csv(df_locations, 'locations')

    # Salvar dados brutos
    save_raw_json(characters, 'characters')
    save_raw_json(episodes, 'episodes')
    save_raw_json(locations, 'locations')
   

if __name__ == '__main__':
    run_pipeline()