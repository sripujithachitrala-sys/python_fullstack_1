from flask import Flask, render_template,request,redirect,url_for,jsonify,session,sqlite3

app=Flask(__name__)

app.secret_key="super_secret_key"

def get_db_connection():
    conn=sqlite3.connect("database.db")
    conn.row_factory=sqlite3.Row #Returns rows as dicts instead of tuples
    return conn

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")  

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/courses")
def courses():
    return render_template("courses.html")

@app.route("/register")
def register():
    return render_template("register.html")   

@app.route("/login")
def login():
    return render_template("login.html")       

@app.route("/trainers")
def trainers():
    return render_template("trainers.html")                      


if __name__=="__main__":
    app.run(debug=True)

