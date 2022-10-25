"""
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

x = "aqua (water), cetearyl alcohol, cetrimonium chloride, dipalmitoylethyl hydroxyethylmonium methosulfate, parfum (fragrance), methoxy peg/ppg-7/3 aminopropyl dimethicone, dipropylene glycol, triethylene glycol, benzyl alcohol, propylene glycol, sodium hydroxide, methylchloroisothiazolinone methylisothiazolinone, magnesium nitrate, magnesium chloride, pisum sativum (pea) peptide, pentaerythrityl tetra-di-t-butyl hydroxyhydrocinnamate, leuconostoc/radish root ferment filtrate"
print(x.lower())

"""