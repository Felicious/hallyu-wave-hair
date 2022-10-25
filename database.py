import sqlite3

con = sqlite3.connect("HairProduct.db")

# executing SQL statements
cur = con.cursor()

cur.execute("""
    CREATE TABLE [IF NOT EXISTS] product_list
    (
        product_id INTEGER PRIMARY KEY, 
        name VARCHAR NOT NULL,
        company VARCHAR
    )
    """)
cur.execute("""
    CREATE TABLE [IF NOT EXISTS] ingredient_list
    (
        ingredient_id INTEGER PRIMARY KEY, 
        name VARCHAR NOT NULL,
        category VARCHAR, 
    )
    """)
cur.execute("""
    CREATE TABLE [IF NOT EXISTS] product_content
    (
        product_id INTEGER,
        ingredient_id INTEGER,
        PRIMARY KEY (product_id, ingredient_id),
        FOREIGN KEY (product_id)
            REFERENCES product_list (product_id)
                ON DELETE CASCADE
                ON UPDATE NO ACTION,
        FOREIGN KEY (ingredient_id)
            REFERENCES ingredient_list (ingredient_id)
                ON DELETE CASCADE
                ON UPDATE NO ACTION
    )
    """)

cur.execute("""
    INSERT INTO product_list(product_id, name, company)
    VALUES
        (0, "Fiber Fix Shampoo", "fanola"),
        (1, "Fiber Fix Bond Connector n2", "fanola"),
        (2, "Elvive Extraordinary Clay Rebalancing Shampoo", "L'Oreal")
""")
"""response = cur.execute("PRAGMA table_info('hair_products')")
print(response.fetchone())"""


