import sqlite3

con = sqlite3.connect("HairProduct.db")

# executing SQL statements
cur = con.cursor()

cur.execute("""
    CREATE TABLE product_list
    (
        product_id INTEGER PRIMARY KEY AUTOINCREMENT, 
        name VARCHAR NOT NULL,
        company VARCHAR
    )
    """)
cur.execute("""
    CREATE TABLE ingredient_list
    (
        ingredient_id INTEGER PRIMARY KEY AUTOINCREMENT, 
        name VARCHAR NOT NULL,
        category VARCHAR 
    )
    """)
cur.execute("""
    CREATE TABLE product_content
    (
        product_id INTEGER,
        ingredient_id INTEGER,
        PRIMARY KEY (product_id, ingredient_id),
        FOREIGN KEY (product_id)
            REFERENCES product_list (product_id)
                ON DELETE CASCADE,
        FOREIGN KEY (ingredient_id)
            REFERENCES ingredient_list (ingredient_id)
                ON DELETE CASCADE
    )
    """)

cur.execute("""
    INSERT INTO product_list(product_id, name, company)
    VALUES
        (0, "Fiber Fix Shampoo", "fanola"),
        (1, "Fiber Fix Bond Connector n2", "fanola"),
        (2, "Elvive Extraordinary Clay Rebalancing Shampoo", "L'Oreal")
""")
cur.execute("""
    INSERT INTO ingredient_list(ingredient_id, name)
    VALUES
        (0, "alpha-isomethyl ionone"),
        (1, "ammonium lauryl sulfate"),
        (2, "aqua / water / eau"),
        (3, "argilla / magnesium aluminum silicate"),
        (4, "benzyl alcohol"),
        (5, "benzyl salicylate"),
        (6, "carbomer"),
        (7, "cetearyl alcohol"),
        (8, "cetrimonium chloride"),
        (9, "ci 42090 / blue 1"),
        (10, "citric acid"),
        (11, "citronellol"),
        (12, "cocamide mea"),
        (13, "coco-betaine"),
        (14, "dipalmitoylethyl hydroxyethylmonium methosulfate"),
        (15, "dipropylene glycol"),
        (16, "fumaric acid"),
        (17, "geraniol"),
        (18, "glycol distearate"),
        (19, "guar hydroxypropyltrimonium chloride"),
        (20, "hexyl cinnamal"),
        (21, "kaolin"),
        (22, "laureth-10"),
        (23, "leuconostoc/radish root ferment filtrate"),
        (24, "linalool"),
        (25, "magnesium chloride"),
        (26, "magnesium nitrate"),
        (27, "methoxy peg/ppg-7/3 aminopropyl dimethicone"),
        (28, "methylchloroisothiazolinone methylisothiazolinone"),
        (29, "mipa-lauryl sulfate"),
        (30, "montmorillonite"),
        (31, "octyldodecanol"),
        (32, "parfum / fragrance"),
        (33, "pentaerythrityl tetra-di-t-butyl hydroxyhydrocinnamate"),
        (34, "pisum sativum (pea) peptide"),
        (35, "ppg-5-ceteth-20"),
        (36, "propylene glycol"),
        (37, "salicylic acid"),
        (38, "sodium benzoate"),
        (39, "sodium chloride"),
        (40, "sodium cocoamphoacetate"),
        (41, "sodium hyaluronate"),
        (42, "sodium hydroxide"),
        (43, "sodium laureth sulfate"),
        (44, "sodium myreth sulfate"),
        (45, "triethylene glycol")
""")
"""response = cur.execute("PRAGMA table_info('hair_products')")
print(response.fetchone())"""


