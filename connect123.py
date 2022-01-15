import sqlite3

def connection(dbname):
    conn=sqlite3.connect("dbname")
    conn.execute("CREATE TABLE IF NOT EXISTS OYO_HOTELS (NAME TEXT, ADDRESS TEXT, PRICE INT, AMENITIES TEXT, RATINGS TEXT)")
    print("Table created succefully!")
    conn.close()

def insert_into_table(dbname,values):
    conn=sqlite3.connect("dbname")
    insert_sql="INSERT INTO OYO_HOTELS ('NAME','ADDRESS','PRICE','AMENITIES','RATINGS') VALUES (?,?,?,?,?)"
    conn.execute(insert_sql,values)
    print("Insterted value into the table :",str(values))
    conn.commit() #to comit to the changes every time we make change
    conn.close()

def get_hotel_info(dbname):
    conn=sqlite3.connect("dbname")
    cur=conn.cursor()
    cur.execute("SELECT * FROM OYO_HOTELS")
    table_data=cur.fetchall()
    for record in table_data:
        print(record)
    conn.close()