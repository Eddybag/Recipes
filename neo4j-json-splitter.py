import json

with open('recipes.json') as data_file:
	data = json.load(data_file)
lista = []
recipes = {}
for i, r in enumerate(data["recipes"]):
	lista.append(r)
	if(i % 200 == 0):
		with open('recipes'+str(i)+'.json', 'w') as outfile:
			recipes['recipes'] = lista
			json.dump(recipes, outfile)
		lista = []	

