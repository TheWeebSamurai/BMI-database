# put the while loop in a mainFunction and check the inputs also in the MainFunction :D

import sqlite3

conn = sqlite3.connect('health.db')
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS students (
            name text,
            age integer,
            weight integer,
            height integer,
            id integer
            )""")


def add():
    name = input("Name: ")
    age = input("Age: ")
    weight = input("Weight: ")
    height = input("Height: ")
    id1 = input("Id: ")
    c.execute(f"INSERT INTO students VALUES ('{name}','{age}','{weight}kg','{height}cm','{id1}')")
    print(f"Name: {name}, Age: {age}, Weight: {weight}, Height: {height}, id: {id1}")
    conn.commit()

def remove():
    id1 = input("Enter in the Id of the person you want to remove from the database: ")
    c.execute(f"DELETE FROM students where id={id1}")
    print('Removed Sucessfully')
    conn.commit()


def mainFunction():
    while True:
        in1 = input("Database options are add, remove, exit, edit, showall: ").lower()

        if in1 == "add":
            add()

        if in1 == "show all":
            print(c.fetchone())

        if in1 == "remove":
            remove()

        
conn.commit()

mainFunction()