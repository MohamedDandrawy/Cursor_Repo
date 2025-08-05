import sqlite3
import os
from datetime import datetime

class Database:
    def __init__(self, db_name="flights.db"):
        self.db_name = db_name
        self.conn = None
        self.cursor = None
        self.create_connection()
        self.create_tables()
    
    def create_connection(self):
        """Create a database connection"""
        try:
            self.conn = sqlite3.connect(self.db_name)
            self.cursor = self.conn.cursor()
            print("Database connection established successfully")
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")
    
    def create_tables(self):
        """Create the reservations table if it doesn't exist"""
        try:
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS reservations (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    flight_number TEXT NOT NULL,
                    departure TEXT NOT NULL,
                    destination TEXT NOT NULL,
                    date TEXT NOT NULL,
                    seat_number TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            self.conn.commit()
            print("Tables created successfully")
        except sqlite3.Error as e:
            print(f"Error creating tables: {e}")
    
    def add_reservation(self, name, flight_number, departure, destination, date, seat_number):
        """Add a new reservation to the database"""
        try:
            self.cursor.execute('''
                INSERT INTO reservations (name, flight_number, departure, destination, date, seat_number)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (name, flight_number, departure, destination, date, seat_number))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Error adding reservation: {e}")
            return False
    
    def get_all_reservations(self):
        """Get all reservations from the database"""
        try:
            self.cursor.execute('SELECT * FROM reservations ORDER BY created_at DESC')
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error fetching reservations: {e}")
            return []
    
    def get_reservation_by_id(self, reservation_id):
        """Get a specific reservation by ID"""
        try:
            self.cursor.execute('SELECT * FROM reservations WHERE id = ?', (reservation_id,))
            return self.cursor.fetchone()
        except sqlite3.Error as e:
            print(f"Error fetching reservation: {e}")
            return None
    
    def update_reservation(self, reservation_id, name, flight_number, departure, destination, date, seat_number):
        """Update an existing reservation"""
        try:
            self.cursor.execute('''
                UPDATE reservations 
                SET name = ?, flight_number = ?, departure = ?, destination = ?, date = ?, seat_number = ?
                WHERE id = ?
            ''', (name, flight_number, departure, destination, date, seat_number, reservation_id))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Error updating reservation: {e}")
            return False
    
    def delete_reservation(self, reservation_id):
        """Delete a reservation by ID"""
        try:
            self.cursor.execute('DELETE FROM reservations WHERE id = ?', (reservation_id,))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Error deleting reservation: {e}")
            return False
    
    def close_connection(self):
        """Close the database connection"""
        if self.conn:
            self.conn.close()
            print("Database connection closed")

# Initialize database
db = Database()