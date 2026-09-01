from flask import Flask, render_template,request,redirect,url_for,jsonify,session
import sqlite3
app=Flask(__name__)

app.secret_key="super_secret_key"

def get_db_connection():
    conn=sqlite3.connect("database.db")
    conn.row_factory=sqlite3.Row #Returns rows as dicts instead of tuples
    return conn

def init_db(): #Initialize the database (create tables if they dont exist)
    conn=get_db_connection()
    cursor=conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT NOT NULL,email TEXT NOT NULL,password TEXT NOT NULL,dob TEXT NOT NULL,gender TEXT NOT NULL,courses TEXT NOT NULL)")
    conn.commit()
    conn.close()
init_db()    


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

@app.route("/api/register",methods=["post"])
def api_register():
    data=request.get_json()
    email=data.get("email")
    conn=get_db_connection()
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM users WHERE email=?",(email,))
    existing_user=cursor.fetchone()
    if existing_user:
        conn.close()
        return jsonify({"message": "Email already registered"}),400
        name=data.get("name")
                                 


if __name__=="__main__":
    app.run(debug=True)

