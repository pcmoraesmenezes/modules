import json
from pprint import pprint
from typing import TypedDict

class Movie(TypedDict):
    
    title: str
    original_title: str 
    is_movie: bool 
    imdb_rating: float
    year: int 
    characters: list[str]
    budget: None | float

#Com o modulo typedDict conseguimos realizar essa tipagem

filme_json = '''
{
  "title": "O Senhor dos Anéis: A Sociedade do Anel",
  "original_title": "The Lord of the Rings: The Fellowship of the Ring",
  "is_movie": true,
  "imdb_rating": 8.8,
  "year": 2001,
  "characters": ["Frodo", "Sam", "Gandalf", "Legolas", "Boromir"],
  "budget": null
}
'''


filme : Movie = json.loads(filme_json)
print(filme['title'])
print(filme['characters'][0])
print(filme['year'])

filme_para_json = json.dumps(filme, ensure_ascii=False, indent=2)
print(filme_para_json)