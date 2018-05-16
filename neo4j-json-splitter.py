import os, requests, json, time 
from requests.utils import requote_uri


def translate_word(word):
	headers = {'Content-Type': 'application/json'}
	url = "http://localhost:8080/api/?tl=es&q="+word
	url = requote_uri(url)
	print(url)
	response = requests.get(url, headers)
	if response.status_code == 200:
		return json.loads(response.content.decode('utf-8'))[0]


def wait(seconds):
	time.sleep(seconds)

def translate_recipe(recipe):
	lista_ingredients = []
	lista_methods = []
	recipe['title']  = translate_word(recipe['title']);
	wait(1)
	recipe['serves']  = translate_word(recipe['serves']);
	
	for i, ing in enumerate(recipe['ingredients']):
		lista_ingredients.append(translate_word(ing))
	
	recipe['ingredients'] = lista_ingredients 
	for i, met in enumerate(recipe['method']):
		lista_methods.append(translate_word(met))
	
	recipe['method'] = lista_methods
	recipe['time']['preparation'] = translate_word(recipe['time']['preparation'])
	recipe['time']['cooking'] = translate_word(recipe['time']['cooking'])

	return recipe


with open('recipes.json') as data_file:
	data = json.load(data_file)
lista = []
recipes = {}
for i, r in enumerate(data["recipes"]):
	if(i > 7660):	
		if(r['title'] is not None and r['title']):
			lista.append(translate_recipe(r))
		if(r['time']['cookingMins'] is None):
			r['time']['cookingMins']=0
		if(r['time']['preparationMins'] is None):	
			r['time']['preparationMins']=0
		if(i % 20 == 0):
			file_name = 'recipes'+str(i)+'.json'
			with open(file_name, 'w') as outfile:
				print('--------------------------- SAVING FILE %s -------------------------------'%(file_name))
				json.dump(lista, outfile)
			lista = []	

