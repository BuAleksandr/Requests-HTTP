import requests

url = "https://superheroapi.com/api/2619421814940190/"

superhero = {}

hero_list = ('Hulk', 'Captain America', 'Thanos')

for name in hero_list:
    response = requests.get(url + f"/search/{name}")
    superhero[name] = response.json()

intelligence = {k: v['results'][0]['powerstats']['intelligence'] for k, v in superhero.items()}
hero_max_intelligence = sorted(intelligence.items(), key=lambda x: int(x[1]))[-1]
print(hero_max_intelligence[0])


