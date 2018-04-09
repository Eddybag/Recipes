import json

with open('recipes.json') as data_file:    
    data = json.load(data_file)

def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]

data = chunks(data, 3)
print(data)
