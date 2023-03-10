# беза данных
# CRUD - create reed update delete
# типы данных в базе данных

# субд - система управления базами данных - oracl,mySQL,POSGREsql
# реляционные - там есть таблицы и легкая связь
# не реляционные - сложные связи, noSQL
# SQL-структурированный язык запросов

import sqlite3

from sqlite3 import Error as e


def create_connection(db_file):
    conn = False
    try:
        conn = sqlite3.connect(db_file)
    except e:
        print('что-то не так')
        print(e)
    return conn


def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except e:
        print(e)


def create_student(conn, student):
    sql = '''INSERT INTO student(fullname,age,hobby,mark,is_working)
    VALUES (?,?,?,?,?)
    '''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, student)
        conn.commit()
    except e:
        print(e)


def reed_students(conn):
    try:
        sql = '''SELECT * FROM student'''
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for i in rows:
            print(i)
    except e:
        print(e)


def update_name_hobby(conn, id, name, hobby):
    sql = '''UPDATE student SET fullname=?,hobby=? WHERE id=?'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (name, hobby, id))
        conn.commit()
    except e:
        print(e)





sql_create_table = '''
CREATE TABLE student(
id INTEGER PRIMARY KEY AUTOINCREMENT,
fullname VARCHAR (102) NOT NULL,
age DATE,
hobby TEXT DEFAULT NULL,
mark DOUBLE (2,1) NOT NULL DEFAULT 0.0,
is_working BOOLEAN DEFAULT FALSE
);
'''

database = r'user.db'

connection = create_connection(database)

if connection is not None:
    print('все отлично')
    create_table(connection, sql_create_table)
    create_student(connection,('рита',2000-9-9,None,39.0,True))
    update_name_hobby(connection, 6, 'Адил', 'rtyghjn')



c = sqlite3.connect('user.db')

c.execute('''UPDATE student SET fullname="Адиль" WHERE rowid=6''')
c.execute('''INSERT INTO student VALUES (8,'beka','2003-06-06','tyu',3.3,True)''')

reed_students(connection)