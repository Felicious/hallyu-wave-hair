import json

# returns ingredients as a list
def parse_ingre(blob):
    x = blob.split(",")
    # remove whitespace
    ingre = []
    for item in x:
        ingre.append(item.strip())
    return ingre
    
f = open('hair_products.json')
data = json.load(f)

dict = {}
for obj in data:
    # saves list of ingredients to the key, name of product
    dict[obj['name']] = parse_ingre(obj['ingredients'])

print(dict)
with open('data.json', 'w') as s:
	s.write(json.dumps(dict, indent = 4))
