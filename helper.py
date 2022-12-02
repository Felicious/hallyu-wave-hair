"""
this is a file that contains scripts that
1. help generate correctly formatted info that goes into the database
"""
import os 
import json

# input is the file dummy, which contains
# ingredients separated by \n as a
# long string w/ ingredients separated by comma
def convert_ingre_list_from_new_line_to_comma():
    with open('dummy', 'r') as f:

        ingredients_list = []
        data = f.readlines()
        for line in data:
            ingredients_list.append(line.strip('\n').lower())

        print(','.join(map(str, ingredients_list)))

    # resulting output, x
    # x = "aqua (water), cetearyl alcohol, cetrimonium chloride, dipalmitoylethyl hydroxyethylmonium methosulfate, parfum (fragrance), methoxy peg/ppg-7/3 aminopropyl dimethicone, dipropylene glycol, triethylene glycol, benzyl alcohol, propylene glycol, sodium hydroxide, methylchloroisothiazolinone methylisothiazolinone, magnesium nitrate, magnesium chloride, pisum sativum (pea) peptide, pentaerythrityl tetra-di-t-butyl hydroxyhydrocinnamate, leuconostoc/radish root ferment filtrate"
    # print(x.lower())

# input: hair products with info stored in hair_products.json
# returns unique ingredients in SQL table insert format, like the following:
#  (ingredient_id, name, category)
def generate_table_of_unique_ingredients():

    f = open('hair_products.json')
    data = json.load(f)

    unique_ingredients = []
    for product in data:
        ingre_list = product['ingredients'].split(", ")
        for ingre in ingre_list:
            if ingre not in unique_ingredients:
                unique_ingredients.append(ingre)

    unique_ingredients.remove("aqua (water)")
    unique_ingredients.remove("parfum (fragrance)")
    unique_ingredients.sort()
    
    # now have to assign ids
    count = 0
    return_string = ""
    for ingre in unique_ingredients:
        line = "({}, \"{}\", \"\")".format(count,ingre)
        count += 1
        return_string += line
    
    print(return_string)

generate_table_of_unique_ingredients()






