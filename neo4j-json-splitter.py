import json

with open('recipes.json') as data_file:
	data = json.load(data_file)
lista = []
recipes = {}
for i, r in enumerate(data["recipes"]):		
	if(r['title'] is not None and r['title']):
		lista.append(r)
	if(r['time']['cookingMins'] is None):
		r['time']['cookingMins']=0
	if(r['time']['preparationMins'] is None):	
		r['time']['preparationMins']=0
	if(i % 50 == 0):
		with open('recipes'+str(i)+'.json', 'w') as outfile:
			json.dump(lista, outfile)
		lista = []	

