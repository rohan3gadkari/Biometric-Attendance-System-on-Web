from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_attendance():
    conn = sqlite3.connect('database/attendance.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM attendance ORDER BY time DESC")
    rows = cur.fetchall()
    conn.close()
    return rows

@app.route("/")
def home():
    records = get_attendance()
    return render_template("index.html", records=records)

if __name__ == "__main__":
    app.run(debug=True)
