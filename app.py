from flask import Flask, request
import sqlite3

app = Flask(__name__)

USERNAME = "admin"
PASSWORD = "admin123"

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        result = cursor.execute(query).fetchone()
        conn.close()

        if result:
            return "Login successful"
        else:
            return "Invalid credentials"
    return '''
        <form method="post">
            Username: <input name="username"><br>
            Password: <input name="password" type="password"><br>
            <input type="submit" value="Login">
        </form>
    '''

if __name__ == "__main__":
    app.run(debug=True)
