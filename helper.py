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
# output
# (0, "alpha-isomethyl ionone", "")(1, "ammonium lauryl sulfate", "")(2, "aqua / water / eau", "")(3, "argilla / magnesium aluminum silicate", "")(4, "benzyl alcohol", "")(5, "benzyl salicylate", "")(6, "carbomer", "")(7, "cetearyl alcohol", "")(8, "cetrimonium chloride", "")(9, "ci 42090 / blue 1", "")(10, "citric acid", "")(11, "citronellol", "")(12, "cocamide mea", "")(13, "coco-betaine", "")(14, "dipalmitoylethyl hydroxyethylmonium methosulfate", "")(15, "dipropylene glycol", "")(16, "fumaric acid", "")(17, "geraniol", "")(18, "glycol distearate", "")(19, "guar hydroxypropyltrimonium chloride", "")(20, "hexyl cinnamal", "")(21, "kaolin", "")(22, "laureth-10", "")(23, "leuconostoc/radish root ferment filtrate", "")(24, "linalool", "")(25, "magnesium chloride", "")(26, "magnesium nitrate", "")(27, "methoxy peg/ppg-7/3 aminopropyl dimethicone", "")(28, "methylchloroisothiazolinone methylisothiazolinone", "")(29, "mipa-lauryl sulfate", "")(30, "montmorillonite", "")(31, "octyldodecanol", "")(32, "parfum / fragrance", "")(33, "pentaerythrityl tetra-di-t-butyl hydroxyhydrocinnamate", "")(34, "pisum sativum (pea) peptide", "")(35, "ppg-5-ceteth-20", "")(36, "propylene glycol", "")(37, "salicylic acid", "")(38, "sodium benzoate", "")(39, "sodium chloride", "")(40, "sodium cocoamphoacetate", "")(41, "sodium hyaluronate", "")(42, "sodium hydroxide", "")(43, "sodium laureth sulfate", "")(44, "sodium myreth sulfate", "")(45, "triethylene glycol", "")






