import sqlite3 as sql

conn = sql.connect('usersdata.db')
# posts = conn.execute("SELECT * FROM students").fetchall()
print(conn.execute("SELECT * FROM users").fetchall())

passw = conn.execute("SELECT password FROM users WHERE username = ?", ("q")).fetchone()
conn.close()
print(passw)