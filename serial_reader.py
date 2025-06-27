import serial
import time
import sqlite3

ser = serial.Serial('COM3', 9600)

conn = sqlite3.connect('database/attendance.db')
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS attendance (id INTEGER, time TEXT)")
conn.commit()

while True:
    data = ser.readline().decode().strip()
    if data.startswith("ID:"):
        uid = int(data.split(":")[1])
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        cur.execute("INSERT INTO attendance VALUES (?, ?)", (uid, timestamp))
        conn.commit()
        print(f"Attendance marked for ID: {uid}")
