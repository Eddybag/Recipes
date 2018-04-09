import json

<<<<<<< HEAD
with open('recipes.json') as data_file:
	data = json.load(data_file)
lista = []
for i, recipes in enumerate(data["recipes"]):
	lista.append(recipes)
	if(i % 2000 == 0):
		with open('recipes'+str(i)+'.json', 'w') as outfile:
			json.dump(lista, outfile)
		lista = []	




=======
with open('recipes.json') as data_file:    
    data = json.load(data_file)

def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]

data = chunks(data, 3)
print(data)
>>>>>>> fd790002da3cd8e76fbcc94a98a65d472ff264a4
