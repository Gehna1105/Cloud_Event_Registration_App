from flask import Flask, request, redirect
import sqlite3
import os

app = Flask(__name__)

DB_NAME = "registrations.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS registrations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT NOT NULL,
            department TEXT NOT NULL,
            batch TEXT NOT NULL,
            ku_id TEXT NOT NULL,
            enrollment_number TEXT NOT NULL,
            event_name TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>College Event Registration</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #667eea, #764ba2);
                margin: 0;
                padding: 0;
                min-height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
            }
            .container {
                background: white;
                padding: 30px;
                border-radius: 18px;
                box-shadow: 0 8px 25px rgba(0,0,0,0.2);
                width: 420px;
            }
            h1 {
                text-align: center;
                color: #4a148c;
                margin-bottom: 20px;
            }
            label {
                font-weight: bold;
                color: #333;
            }
            input, select {
                width: 100%;
                padding: 10px;
                margin: 8px 0 16px 0;
                border: 1px solid #ccc;
                border-radius: 10px;
                font-size: 14px;
            }
            button {
                width: 100%;
                background: #6a1b9a;
                color: white;
                border: none;
                padding: 12px;
                border-radius: 10px;
                font-size: 16px;
                cursor: pointer;
                font-weight: bold;
            }
            button:hover {
                background: #4a148c;
            }
            .view-link {
                display: block;
                margin-top: 15px;
                text-align: center;
                text-decoration: none;
                color: #6a1b9a;
                font-weight: bold;
            }
            .view-link:hover {
                text-decoration: underline;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🎓 College Event Registration</h1>
            <form action="/register" method="post">
                <label>Full Name:</label>
                <input type="text" name="full_name" required>

                <label>Department:</label>
                <input type="text" name="department" required>

                <label>Batch:</label>
                <input type="text" name="batch" required>

                <label>KU ID:</label>
                <input type="text" name="ku_id" required>

                <label>Enrollment Number:</label>
                <input type="text" name="enrollment_number" required>

                <label>Select Event:</label>
                <select name="event_name" required>
                    <option value="">-- Select an Event --</option>
                    <option value="Hackathon">Hackathon</option>
                    <option value="AI Workshop">AI Workshop</option>
                    <option value="Cultural Fest">Cultural Fest</option>
                    <option value="Robotics Competition">Robotics Competition</option>
                    <option value="Cyber Forensic Seminar">Cyber Forensic Seminar</option>
                    <option value="Lok Sabha">Lok Sabha</option>
                    <option value="ARVR">ARVR</option>
                    <option value="Treasure Hunt">Treasure Hunt</option>
                    <option value="Cooking Contest">Cooking Contest</option>
                </select>

                <button type="submit">Register</button>
            </form>

            <a class="view-link" href="/view">📋 View Registrations</a>
        </div>
    </body>
    </html>
    """

@app.route("/register", methods=["POST"])
def register():
    full_name = request.form["full_name"]
    department = request.form["department"]
    batch = request.form["batch"]
    ku_id = request.form["ku_id"]
    enrollment_number = request.form["enrollment_number"]
    event_name = request.form["event_name"]

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO registrations 
        (full_name, department, batch, ku_id, enrollment_number, event_name)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (full_name, department, batch, ku_id, enrollment_number, event_name))
    conn.commit()
    conn.close()

    return """
    <html>
    <head>
        <title>Success</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #43cea2, #185a9d);
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }
            .box {
                background: white;
                padding: 30px;
                border-radius: 18px;
                box-shadow: 0 8px 25px rgba(0,0,0,0.2);
                text-align: center;
                width: 400px;
            }
            h2 {
                color: #1b5e20;
            }
            a {
                display: inline-block;
                margin-top: 15px;
                text-decoration: none;
                color: white;
                background: #1565c0;
                padding: 10px 18px;
                border-radius: 10px;
                font-weight: bold;
            }
            a:hover {
                background: #0d47a1;
            }
        </style>
    </head>
    <body>
        <div class="box">
            <h2>✅ Registration Successful!</h2>
            <p>Thank you for registering.</p>
            <a href="/">Go Back</a>
        </div>
    </body>
    </html>
    """

@app.route("/view")
def view_registrations():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT full_name, department, batch, ku_id, enrollment_number, event_name FROM registrations")
    rows = cursor.fetchall()
    conn.close()

    table_rows = ""
    for row in rows:
        table_rows += f"""
        <tr>
            <td>{row[0]}</td>
            <td>{row[1]}</td>
            <td>{row[2]}</td>
            <td>{row[3]}</td>
            <td>{row[4]}</td>
            <td>{row[5]}</td>
        </tr>
        """

    return f"""
    <html>
    <head>
        <title>View Registrations</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #ffecd2, #fcb69f);
                margin: 0;
                padding: 30px;
            }}
            h1 {{
                text-align: center;
                color: #6d4c41;
            }}
            table {{
                width: 100%;
                border-collapse: collapse;
                background: white;
                border-radius: 12px;
                overflow: hidden;
                box-shadow: 0 6px 20px rgba(0,0,0,0.15);
            }}
            th, td {{
                padding: 12px;
                border-bottom: 1px solid #ddd;
                text-align: center;
            }}
            th {{
                background: #6a1b9a;
                color: white;
            }}
            tr:hover {{
                background: #f3e5f5;
            }}
            .back {{
                display: block;
                width: 200px;
                margin: 20px auto;
                text-align: center;
                text-decoration: none;
                background: #6a1b9a;
                color: white;
                padding: 12px;
                border-radius: 10px;
                font-weight: bold;
            }}
            .back:hover {{
                background: #4a148c;
            }}
        </style>
    </head>
    <body>
        <h1>📋 Registered Students</h1>
        <table>
            <tr>
                <th>Full Name</th>
                <th>Department</th>
                <th>Batch</th>
                <th>KU ID</th>
                <th>Enrollment Number</th>
                <th>Event Name</th>
            </tr>
            {table_rows}
        </table>
        <a class="back" href="/">⬅ Back to Home</a>
    </body>
    </html>
    """

# Initialize DB automatically when app starts
init_db()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
