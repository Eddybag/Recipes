import json

with open('recipes.json') as data_file:
	data = json.load(data_file)
lista = []
for i, recipes in enumerate(data["recipes"]):
	lista.append(recipes)
	if(i % 2000 == 0):
		with open('recipes'+str(i)+'.json', 'w') as outfile:
			json.dump(lista, outfile)
		lista = []	




