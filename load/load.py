from sqlalchemy import create_engine
import json
import os

def save_as_parquet(df, filename):
    try:
        os.makedirs('data/processed', exist_ok=True)
        df.to_parquet(f"data/processed/{filename}.parquet", index=False)
        print(f"Arquivo salvo: data/processed/{filename}.parquet")
    except Exception as e:
        print(f'Falha ao salvar {filename} em parquet: {e}')

def save_as_db(db_key, df, filename):
    try:
        engine = create_engine(db_key)
        df.to_sql(filename, con=engine, if_exists='replace', index=False)
        print(f'Arquivo salvo no banco de dados')

    except Exception as e:
        print(f'Falha ao carregar no banco de dados: {e}')


def save_as_csv(df, filename):
    try:
        os.makedirs('data/export/', exist_ok=True)
        df.to_csv(f'data/export/{filename}.csv', index=False)
        print(f'Arquivo Salvo: data/export/{filename}.csv')

    except Exception as e:
        print(f'Falha ao salvar {filename} em csv: {e}')

def save_raw_json(data, filename):
    try:
        os.makedirs('data/raw', exist_ok=True)
        with open(f'data/raw/{filename}.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f'Arquivo salvo: data/raw/{filename}.json')
    except Exception as e:
        print(f'Falha ao salvar {filename}.json: {e}')

