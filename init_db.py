import sqlite3

# 1. Connect to the database (This will automatically create 'clockit.db' if it doesn't exist)
conn = sqlite3.connect('clockit.db')

# 2. Create a 'cursor' (the tool that actually executes the SQL commands)
cursor = conn.cursor()

print("Connected to SQLite. Building tables...")

# 3. Create the Employees Table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Employees (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Name TEXT NOT NULL,
        Card_UID TEXT UNIQUE NOT NULL,
        Department TEXT,
        Role TEXT
    )
''')
print("- 'Employees' table is ready.")

# 4. Create the Attendance Logs Table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Attendance_Logs (
        Log_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Card_UID TEXT NOT NULL,
        Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        Event_Type TEXT NOT NULL,
        Flagged_Anomaly BOOLEAN DEFAULT 0,
        FOREIGN KEY (Card_UID) REFERENCES Employees(Card_UID)
    )
''')
print("- 'Attendance_Logs' table is ready.")

# 5. Save (commit) the changes and close the connection
conn.commit()
conn.close()

print("Database initialized successfully!")