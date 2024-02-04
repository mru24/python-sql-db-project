import sqlite3
import tkinter as tk
import datetime

connection = sqlite3.connect('mydata.db')
cursor = connection.cursor()

def db_connect():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS devices (
            brand TEXT NOT NULL,
            name TEXT NOT NULL,
            model TEXT,
            info CHAR(120),
            added timestamp
        )            
    """)

def db_insert():
    brand = brandEntry.get()
    name = nameEntry.get()
    model = modelEntry.get()
    info = infoEntry.get()
    added = datetime.datetime.now()
    cursor.execute("""
    INSERT INTO devices VALUES
    ('{}','{}','{}','{}','{}')                                      
    """.format(brand,name,model,info,added))
    connection.commit()

    displayData()

    brandEntry.delete(0,'end')
    nameEntry.delete(0,'end')
    modelEntry.delete(0,'end')
    infoEntry.delete(0,'end')    

# query = "SELECT * FROM devices"
def db_select(query):
    cursor.execute(query)

def get_rows():
    return cursor.fetchall()

def db_close():    
    connection.close()

def displayData():
    db_select("SELECT * FROM devices")
    for index,row in enumerate(get_rows()):
        brandFields.append(tk.Entry(dbFrame,font=ef))
        brandFields[index].grid(row=index+1,column=0)
        brandFields[index].delete(0,'end')
        brandFields[index].insert(0,row[0])

        nameFields.append(tk.Entry(dbFrame,font=ef))
        nameFields[index].grid(row=index+1,column=1)
        nameFields[index].delete(0,'end')
        nameFields[index].insert(0,row[1])

        modelFields.append(tk.Entry(dbFrame,font=ef))
        modelFields[index].grid(row=index+1,column=2)
        modelFields[index].delete(0,'end')
        modelFields[index].insert(0,row[2])

        infoFields.append(tk.Entry(dbFrame,font=ef))
        infoFields[index].grid(row=index+1,column=3)
        infoFields[index].delete(0,'end')
        infoFields[index].insert(0,row[3])     

        addedFields.append(tk.Entry(dbFrame,font=ef))
        addedFields[index].grid(row=index+1,column=4)
        addedFields[index].delete(0,'end')
        addedFields[index].insert(0,row[4])   

root = tk.Tk()
root.geometry("800x400")

ef = ('calibre',12, 'bold')
bf = ('calibre',10, 'bold')

brandFields = []
nameFields = []
modelFields = []
infoFields = []
addedFields = []

topFrame = tk.Frame(root)
dbFrame = tk.Frame(root)
bottomFrame = tk.Frame(root)

brandLabel = tk.Label(dbFrame,text='Brand').grid(row=0,column=0)
nameLabel = tk.Label(dbFrame,text='Name').grid(row=0,column=1)
modelLabel = tk.Label(dbFrame,text='Model').grid(row=0,column=2)
infoLabel = tk.Label(dbFrame,text='Description').grid(row=0,column=3)
addedLabel = tk.Label(dbFrame,text='Date added').grid(row=0,column=4)

nameEntry = tk.Entry(bottomFrame,font=ef)
nameEntry.grid(row=0,column=0)
brandEntry = tk.Entry(bottomFrame,font=ef)
brandEntry.grid(row=0,column=1)
modelEntry = tk.Entry(bottomFrame,font=ef)
modelEntry.grid(row=0,column=2)
infoEntry = tk.Entry(bottomFrame,font=ef)
infoEntry.grid(row=0,column=3)

addButton = tk.Button(bottomFrame,text="Add new",font=bf,command=db_insert)
addButton.grid(row=1,column=0)

topFrame.pack(padx=5,pady=5)
dbFrame.pack(padx=5,pady=5)
bottomFrame.pack(padx=5,pady=5)

db_connect()  
displayData() 

root.mainloop()