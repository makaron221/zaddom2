from app import app
from flask import render_template, url_for,\
redirect, flash, session, request
import sqlite3
from app.forms import LoginForm
from app.config import Config

app.config.from_object(Config)
logged = False
PIC = "data:image/png;base64,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"


@app.route("/register", methods=["GET", "POST"])
def register():
    
    message = ''
    account = False
    if request.method == "POST" and 'username' in request.form \
    and 'email' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

        conn = sqlite3.connect("usersdata.db")
        try:
            account = conn.execute("SELECT * FROM users WHERE username = ?", (username)).fetchall()#% s
        except:
            pass

        if not username or not password or not email:
            message = "you haven\'t filled the form"

        elif account:
            message = "acount already exist"
        
        else:
            conn.execute("INSERT INTO users VALUES(?, ?, ?)", (username, email, password))
            conn.execute("INSERT INTO pictures VALUES(?, ?)", (username, PIC))
            conn.commit()
            conn.close()
            message = "you\'ve registered"
            return redirect(url_for("loginv2"))
    flash(message)
    return render_template("register.html", title_="register")


@app.route("/loginv2", methods = ["GET", "POST"])
def loginv2():
    global logged
    if request.method == "POST" and 'username' in request.form and 'password' in request.form:
        username = request.form["username"]
        password = request.form["password"]
        if not username or not password:
            return render_template("loginv2.html")
        conn = sqlite3.connect("usersdata.db")
        passw = conn.execute("SELECT password FROM users WHERE username = ?", (username)).fetchone()
        conn.close()
        if password == passw[0]:
            logged = True
            session["username"] = username
            return redirect(url_for("chat"))
    return render_template("loginv2.html")



@app.route("/chat", methods=["GET", "POST"])
def chat():
    global logged
    if logged == False:
        return redirect(url_for("loginv2"))
    
    conn = sqlite3.connect("usersdata.db")

    if request.method == "POST" and 'write' in request.form:
        text = request.form['write']
        conn.execute("INSERT INTO posts VALUES(?, ?)", (session["username"], text))
        conn.commit()

    posts = conn.execute("SELECT * FROM posts").fetchall()
    picss = conn.execute("SELECT * FROM pictures").fetchall()
    pics = {}
    for i in picss:
        pics[i[0]] = i[1]
    conn.close()
    return render_template('chat.html', num=len(posts), posts=posts, pics=pics)

@app.route("/settings", methods=["GET", "POST"])
def settings():
    global logged
    if logged != True:
        return redirect(url_for("loginv2"))
    
    conn = sqlite3.connect("usersdata.db")

    if request.method == "POST":
        if "picture" in request.form:
            conn.execute("DELETE FROM pictures WHERE username = ?", (session["username"]))
            conn.execute("INSERT INTO pictures VALUES(?, ?)", (session["username"], request.form["picture"]))
            conn.commit()
        # if "username" in request.form:
            # data = conn.execute("SELECT * FROM users WHERE username = ?", (session['username'])).fetchone()
            # conn.execute("DELETE FROM users WHERE username = ?", (session['username']))
            # conn.execute("INSERT INTO users VALUES(?, ?, ?)", (request.form['username'], data[1], data[2]))
            # picdata = conn.execute("SELECT picture FROM pictures WHERE username = ?", (session['username'])).fetchone()[0]
            # conn.execute("DELETE FROM pictures WHERE username = ?", (session['username']))
            # conn.execute("INSERT INTO pictures VALUES(?, ?)", (request.form['username'], picdata))
            # conn.commit()
            # session['username'] = request.form['username']
            # #change username in pictures

    pic = conn.execute("SELECT picture FROM pictures WHERE username = ?", (session["username"])).fetchone()[0]
    return render_template("settings.html", username=session["username"], pic=pic)
    





@app.route("/logout")
def logout():
    global logged
    logged = False
    return redirect('/')
    




@app.route("/")
@app.route("/home")
def index():
    return render_template("index.html")







    #     if account:
    #         session["loggedin"] = True
    #         session['id'] = account["id"]
    #         session["username"] = account["username"]
    #         msg = "you are logged in"
    #     else:
    #         msg = "incorrect username or password"
    #     flash(msg)
    # return render_template("loginv2.html", form=form)