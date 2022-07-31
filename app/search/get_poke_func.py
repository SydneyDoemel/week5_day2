import requests
import pprint 
pp = pprint.PrettyPrinter(indent=4)

def get_poke_func(poke_you_want):
 
        url = f"https://pokeapi.co/api/v2/pokemon/{poke_you_want}"
        response = requests.get(url)

        data = response.json()
        get_data = []
        poke_dict = {}
        poke_name = data['forms'][0]['name']
        poke_dict[poke_name] = {
            'Name' : data['forms'][0]['name'],
            'Ability' : data['abilities'][0]['ability']['name'],
            'Base Experience' : data['base_experience'],
            'front_shiny URL' : data['sprites']['front_shiny'],
            'attack base_stat' : data['stats'][1]['base_stat'],
            'hp base_stat' : data['stats'][0]['base_stat'],
            'defense base_stat': data['stats'][2]['base_stat']
            }
            
        get_data.append(poke_dict)
        return get_data
   