import sqlite3

db = sqlite3.connect('users.db')

c = db.cursor()

c.execute(""" CREATE TABLE IF NOT EXISTS user(
name text,
age integer,
mark integer,
status text
)
""");

c.execute("INSERT INTO user VALUES('Самат','самата нет',10,'Samat')")

c.execute("UPDATE user SET name = 'Zahro' WHERE rowid=1")
c.execute("UPDATE user SET name = 'Zahro' WHERE name='Lena'")
c.execute("UPDATE user SET name = 'x' WHERE rowid > 3")
c.execute("UPDATE user SET mark = 11 WHERE mark = 10")
c.execute("UPDATE user SET status = 'maker' WHERE rowid=3 ")

c.execute("DELETE FROM user WHERE rowid <> 3")



c.execute("SELECT rowid,* FROM user") 
item = c.fetchall()
for el in item:
    print(el)

db.commit()
db.close()
