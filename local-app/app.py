from flask import Flask, request
import sqlite3
import os

app = Flask(__name__)

# Create database folder if it doesn't exist
if not os.path.exists("database"):
    os.makedirs("database")

DB_PATH = "database/registrations.db"

# Create table if not exists
def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS registrations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT NOT NULL,
            ku_id TEXT NOT NULL,
            enrollment_number TEXT NOT NULL,
            department TEXT NOT NULL,
            batch TEXT NOT NULL,
            event_name TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

init_db()

@app.route("/", methods=["GET", "POST"])
def register():
    message = ""

    if request.method == "POST":
        full_name = request.form.get("full_name")
        ku_id = request.form.get("ku_id")
        enrollment_number = request.form.get("enrollment_number")
        department = request.form.get("department")
        batch = request.form.get("batch")
        event_name = request.form.get("event_name")

        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO registrations 
            (full_name, ku_id, enrollment_number, department, batch, event_name)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (full_name, ku_id, enrollment_number, department, batch, event_name))
        conn.commit()
        conn.close()

        message = "🎉 Registration Successful! Your event entry has been recorded."

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>College Event Registration</title>
        <style>
            * {{
                box-sizing: border-box;
                margin: 0;
                padding: 0;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            }}

            body {{
                background: linear-gradient(135deg, #1e3c72, #2a5298, #6a11cb, #2575fc);
                min-height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                padding: 30px;
            }}

            .container {{
                background: rgba(255, 255, 255, 0.95);
                width: 100%;
                max-width: 550px;
                padding: 35px;
                border-radius: 20px;
                box-shadow: 0 15px 35px rgba(0, 0, 0, 0.25);
                backdrop-filter: blur(8px);
            }}

            h1 {{
                text-align: center;
                color: #1e3c72;
                margin-bottom: 10px;
                font-size: 28px;
            }}

            .subtitle {{
                text-align: center;
                color: #555;
                margin-bottom: 25px;
                font-size: 14px;
            }}

            label {{
                font-weight: 600;
                color: #333;
                display: block;
                margin-bottom: 6px;
                margin-top: 12px;
            }}

            input, select {{
                width: 100%;
                padding: 12px;
                border: 2px solid #dcdcdc;
                border-radius: 10px;
                font-size: 15px;
                outline: none;
                transition: 0.3s;
                background-color: #f9f9f9;
            }}

            input:focus, select:focus {{
                border-color: #6a11cb;
                background-color: #fff;
                box-shadow: 0 0 8px rgba(106, 17, 203, 0.2);
            }}

            button {{
                width: 100%;
                margin-top: 22px;
                padding: 14px;
                border: none;
                border-radius: 12px;
                background: linear-gradient(90deg, #6a11cb, #2575fc);
                color: white;
                font-size: 16px;
                font-weight: bold;
                cursor: pointer;
                transition: 0.3s ease;
            }}

            button:hover {{
                transform: translateY(-2px);
                box-shadow: 0 8px 20px rgba(37, 117, 252, 0.35);
            }}

            .secondary-btn {{
                display: block;
                width: 100%;
                margin-top: 12px;
                padding: 14px;
                text-align: center;
                border-radius: 12px;
                background: #f1f3f6;
                color: #1e3c72;
                font-size: 15px;
                font-weight: bold;
                text-decoration: none;
                border: 2px solid #dcdcdc;
                transition: 0.3s;
            }}

            .secondary-btn:hover {{
                background: #e6ebf5;
            }}

            .success {{
                margin-top: 18px;
                padding: 12px;
                background-color: #eafaf1;
                border: 1px solid #2ecc71;
                color: #1e8449;
                border-radius: 10px;
                text-align: center;
                font-weight: 600;
            }}

            .footer-note {{
                text-align: center;
                margin-top: 18px;
                font-size: 12px;
                color: #666;
            }}

            table {{
                width: 100%;
                border-collapse: collapse;
                margin-top: 20px;
                font-size: 14px;
            }}

            th, td {{
                border: 1px solid #ddd;
                padding: 10px;
                text-align: center;
            }}

            th {{
                background: #2575fc;
                color: white;
            }}

            tr:nth-child(even) {{
                background: #f8f9fa;
            }}

            .table-container {{
                overflow-x: auto;
                margin-top: 15px;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🎓 College Event Registration</h1>
            <p class="subtitle">Register now for exciting university events!</p>

            <form method="POST">
                <label>Full Name</label>
                <input type="text" name="full_name" placeholder="Enter your full name" required>

                <label>KU ID</label>
                <input type="text" name="ku_id" placeholder="Enter your KU ID" required>

                <label>Enrollment Number</label>
                <input type="text" name="enrollment_number" placeholder="Enter enrollment number" required>

                <label>Department</label>
                <select name="department" required>
                    <option value="">Select Department</option>
                    <option value="Computer Engineering">Computer Engineering</option>
                    <option value="Information Technology">Information Technology</option>
                    <option value="Cyber Security">Cyber Security</option>
                    <option value="Mechanical Engineering">Mechanical Engineering</option>
                    <option value="Civil Engineering">Civil Engineering</option>
                    <option value="Electronics & Communication">Electronics & Communication</option>
                    <option value="MBA">MBA</option>
                    <option value="BBA">BBA</option>
                </select>

                <label>Batch</label>
                <select name="batch" required>
                    <option value="">Select Batch</option>
                    <option value="2022-2026">2022-2026</option>
                    <option value="2023-2027">2023-2027</option>
                    <option value="2024-2028">2024-2028</option>
                    <option value="2025-2029">2025-2029</option>
                </select>

                <label>Select Event</label>
                <select name="event_name" required>
                    <option value="">Select Event</option>
                    <option value="Tech Fest">Tech Fest</option>
                    <option value="Cultural Event">Cultural Event</option>
                    <option value="Workshop">Workshop</option>
                    <option value="Cyber Forensic Seminar">Cyber Forensic Seminar</option>
                    <option value="Lok Sabha">Lok Sabha</option>
                    <option value="ARVR">ARVR</option>
                    <option value="Treasure Hunt">Treasure Hunt</option>
                    <option value="Cooking Contest">Cooking Contest</option>
                </select>

                <button type="submit">Register Now</button>
            </form>

            {f'<div class="success">{message}</div>' if message else ''}

            <a href="/view" class="secondary-btn">📋 View All Registrations</a>

            <p class="footer-note">Designed for University Event Registration System</p>
        </div>
    </body>
    </html>
    """

@app.route("/view")
def view_registrations():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT full_name, ku_id, enrollment_number, department, batch, event_name
        FROM registrations
        ORDER BY id DESC
    """)
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

    if not rows:
        table_rows = """
        <tr>
            <td colspan="6">No registrations yet.</td>
        </tr>
        """

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>View Registrations</title>
        <style>
            * {{
                box-sizing: border-box;
                margin: 0;
                padding: 0;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            }}

            body {{
                background: linear-gradient(135deg, #141e30, #243b55);
                min-height: 100vh;
                padding: 30px;
            }}

            .container {{
                background: white;
                max-width: 1200px;
                margin: auto;
                padding: 30px;
                border-radius: 20px;
                box-shadow: 0 12px 30px rgba(0, 0, 0, 0.25);
            }}

            h1 {{
                text-align: center;
                color: #1e3c72;
                margin-bottom: 10px;
            }}

            .subtitle {{
                text-align: center;
                color: #555;
                margin-bottom: 25px;
            }}

            .table-container {{
                overflow-x: auto;
            }}

            table {{
                width: 100%;
                border-collapse: collapse;
                font-size: 14px;
            }}

            th, td {{
                border: 1px solid #ddd;
                padding: 12px;
                text-align: center;
            }}

            th {{
                background: linear-gradient(90deg, #6a11cb, #2575fc);
                color: white;
            }}

            tr:nth-child(even) {{
                background-color: #f9f9f9;
            }}

            tr:hover {{
                background-color: #eef4ff;
            }}

            .back-btn {{
                display: inline-block;
                margin-top: 20px;
                padding: 12px 20px;
                border-radius: 10px;
                background: #2575fc;
                color: white;
                text-decoration: none;
                font-weight: bold;
            }}

            .back-btn:hover {{
                background: #1e63d6;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>📋 All Event Registrations</h1>
            <p class="subtitle">Admin view of all submitted student registrations</p>

            <div class="table-container">
                <table>
                    <tr>
                        <th>Full Name</th>
                        <th>KU ID</th>
                        <th>Enrollment Number</th>
                        <th>Department</th>
                        <th>Batch</th>
                        <th>Event Name</th>
                    </tr>
                    {table_rows}
                </table>
            </div>

            <a href="/" class="back-btn">⬅ Back to Registration</a>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
