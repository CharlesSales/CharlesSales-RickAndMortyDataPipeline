import requests as rq

def get_api_data(url: str):
    try:
        response = rq.get(url)
        if response.status_code == 200:
            print(f'Solicitação bem sucedida {response.status_code}')
            return response.json()
        
        else:
            print(f'erro {response.status_code} ao acessar {url}')
            return None
        
    except Exception as e:
        print(f'Erro durante a requisição {e}')
        return None


def fetch_all_endpoints(base_url, max_records=100):
    all_data = []
    page = 1

    while len(all_data) <= max_records:
        print(f"Coletando página {page}...")

        response = rq.get(f"{base_url}?page={page}")

        if response.status_code != 200:
            print(f"Erro na requisição: {response.status_code}")
            break

        data = response.json()
        results = data.get("results", [])
        
        if not results:
            break
        
        all_data.extend(results)

        # Se passou o limite desejado, corta
        if len(all_data) >= max_records:
            all_data = all_data[:max_records]
            break

        # Avança para próxima página
        page += 1

    print(f"Total extraído: {len(all_data)} registros")
    return all_data
 
#def fetch_all_endpoints(url):
    chracter = get_api_data(url)
    locations = get_api_data(url)
    episodes = get_api_data(url)

    return chracter, locations, episodes
