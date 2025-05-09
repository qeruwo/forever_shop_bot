import sqlite3

def create_table():
    conn = sqlite3.connect("iconst_bd.db")
    cur = conn.cursor()
    
    cur.execute("""CREATE TABLE IF NOT EXISTS icons(
        id INTEGER NOT NULL PRIMARY KEY,
        image BLOB,
        name TEXT NOT NULL,
        description TEXT,
        chapter TEXT,
        color TEXT,
        quantity INTEGER,
        price INTEGER,
        is_buying INTEGER
        )""")
    conn.commit()
    cur.close()
    conn.close()
    
    #1 - buying, 0 - no
    #if 0 - so there's nothing
    
    
#catalog

def counting_records_icons():
    conn = sqlite3.connect("iconst_bd.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM icons WHERE chapter = 'icon'")
    count = cur.fetchall()
    return count
