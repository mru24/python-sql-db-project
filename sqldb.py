import sqlite3
import tkinter as tk

connection = sqlite3.connect('mydata.db')
cursor = connection.cursor()

def db_connect():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS devices (
        brand TEXT,
        name TEXT,
        model TEXT,
        descr TEXT
    )            
    """)

def db_insert(a,b,c,d):
    cursor.execute("""
    INSERT INTO devices VALUES
    ('Commodore', 'Amiga', '600', 'lorem ipsum'),
    ('Commodore', 'Amiga', '1200', ''),
    ('Sinclair', 'ZX Spectrum', '', '')
    """)

# query = "SELECT * FROM devices"
def db_select(query):
    cursor.execute(query)

def get_rows():
    return cursor.fetchall()

def db_close():
    connection.commit()
    connection.close()

root = tk.Tk()
root.geometry("800x400")

# brandFrame = tk.Frame(root)
# nameFrame = tk.Frame(root)
# modelFrame = tk.Frame(root)
# infoFrame = tk.Frame(root)

ef = ('calibre',12, 'bold')

brandFields = []
nameFields = []
modelFields = []
infoFields = []

db_select("SELECT * FROM devices")

for index,row in enumerate(get_rows()):
    brandFields.append(tk.Entry(root,font=ef))
    brandFields[index].grid(row=index,column=0)
    brandFields[index].insert(0,row[0])

    nameFields.append(tk.Entry(root,font=ef))
    nameFields[index].grid(row=index,column=1)
    nameFields[index].insert(0,row[1])

    modelFields.append(tk.Entry(root,font=ef))
    modelFields[index].grid(row=index,column=2)
    modelFields[index].insert(0,row[2])

    infoFields.append(tk.Entry(root,font=ef))
    infoFields[index].grid(row=index,column=3)
    infoFields[index].insert(0,row[3])

db_close()

# brandFrame.pack(side="left")
# nameFrame.pack(side="left")
# modelFrame.pack(side="left")
# infoFrame.pack(side="left")

root.mainloop()