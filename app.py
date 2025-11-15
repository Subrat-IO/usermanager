from flask import Flask, render_template, request, redirect
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)


def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",        
            user="root",
            password="Subrat@123",   
            database="users"        
        )
        return connection
    except Error as e:
        print("❌ Error connecting to MySQL:", e)
        return None



@app.route("/hello")
def hello():
    return "Hello World!"



@app.route("/users")
def users():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template("users.html", users=data)


@app.route("/new_user", methods=["GET", "POST"])
def new_user():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        role = request.form["role"]

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO users (name, email, role) VALUES (%s, %s, %s)",
            (name, email, role)
        )
        conn.commit()
        cursor.close()
        conn.close()
        return redirect("/users")
    return render_template("new_user.html")


@app.route("/users/<int:id>")
def user_details(id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE id = %s", (id,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    if not user:
        return "User not found", 404
    return render_template("user_details.html", user=user)



if __name__ == "__main__":
    app.run(debug=True)
