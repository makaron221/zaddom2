import sqlite3
conn = sqlite3.connect("usersdata.db")
conn.execute("CREATE TABLE users(username, email, password)")
conn.execute("CREATE TABLE posts(username, content)")
conn.execute("CREATE TABLE pictures(username, picture)")
conn.commit()
conn.close()