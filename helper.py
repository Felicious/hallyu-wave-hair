# prints ingredients separated by \n as a
# long string w/ ingredients separated by comma

# this is to format the text to save in "ingredients" field
# in hair_products.json
import os 

with open('dummy', 'r') as f:

    ingredients_list = []
    data = f.readlines()
    for line in data:
        ingredients_list.append(line.strip('\n').lower())

    print(','.join(map(str, ingredients_list)))