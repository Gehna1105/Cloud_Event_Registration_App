from flask import Flask, request
import sqlite3
import os

app = Flask(__name__)

DB_FOLDER = "database"
DB_PATH = os.path.join(DB_FOLDER, "registrations.db")

os.makedirs(DB_FOLDER, exist_ok=True)

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS registrations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT NOT NULL,
            event_name TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

init_db()

@app.route("/", methods=["GET", "POST"])
def home():
    message = ""

    if request.method == "POST":
        full_name = request.form.get("full_name")
        event_name = request.form.get("event_name")

        if full_name and event_name:
            conn = sqlite3.connect(DB_PATH)
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO registrations (full_name, event_name) VALUES (?, ?)",
                (full_name, event_name)
            )
            conn.commit()
            conn.close()
            message = "Registration successful!"

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>College Event Registration</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background: #f4f6f9;
                padding: 40px;
            }}
            .container {{
                max-width: 500px;
                margin: auto;
                background: white;
                padding: 25px;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0,0,0,0.1);
            }}
            h1 {{
                text-align: center;
                color: #333;
            }}
            input, select, button {{
                width: 100%;
                padding: 10px;
                margin-top: 10px;
                margin-bottom: 15px;
                border-radius: 6px;
                border: 1px solid #ccc;
            }}
            button {{
                background: #2d89ef;
                color: white;
                border: none;
                cursor: pointer;
            }}
            .success {{
                color: green;
                font-weight: bold;
                text-align: center;
            }}
            .view-link {{
                display: block;
                text-align: center;
                margin-top: 15px;
                text-decoration: none;
                color: #2d89ef;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>College Event Registration</h1>
            <form method="POST">
                <input type="text" name="full_name" placeholder="Enter Full Name" required>
                <select name="event_name" required>
                    <option value="">Select Event</option>
                    <option value="Tech Fest">Tech Fest</option>
                    <option value="Cultural Event">Cultural Event</option>
                    <option value="Workshop">Workshop</option>
                </select>
                <button type="submit">Register</button>
            </form>
            <p class="success">{message}</p>
            <a class="view-link" href="/registrations">View Registrations</a>
        </div>
    </body>
    </html>
    """
    return html

@app.route("/registrations")
def view_registrations():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT full_name, event_name FROM registrations")
    data = cursor.fetchall()
    conn.close()

    rows = ""
    for full_name, event_name in data:
        rows += f"<tr><td>{full_name}</td><td>{event_name}</td></tr>"

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Registrations</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background: #f4f6f9;
                padding: 40px;
            }}
            .container {{
                max-width: 700px;
                margin: auto;
                background: white;
                padding: 25px;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0,0,0,0.1);
            }}
            h1 {{
                text-align: center;
                color: #333;
            }}
            table {{
                width: 100%;
                border-collapse: collapse;
                margin-top: 20px;
            }}
            table, th, td {{
                border: 1px solid #ccc;
            }}
            th, td {{
                padding: 10px;
                text-align: center;
            }}
            a {{
                display: block;
                text-align: center;
                margin-top: 20px;
                color: #2d89ef;
                text-decoration: none;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Registered Students</h1>
            <table>
                <tr>
                    <th>Full Name</th>
                    <th>Event Name</th>
                </tr>
                {rows}
            </table>
            <a href="/">Back to Registration</a>
        </div>
    </body>
    </html>
    """
    return html

if __name__ == "__main__":
    app.run(debug=True)
