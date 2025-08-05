import tkinter as tk
from tkinter import ttk, messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from datetime import datetime
from database import db

class BookingPage:
    def __init__(self, parent, show_home_page):
        self.parent = parent
        self.show_home_page = show_home_page
        self.frame = None
        self.create_widgets()
    
    def create_widgets(self):
        """Create the booking page widgets"""
        # Main frame
        self.frame = ttk.Frame(self.parent, padding="20")
        
        # Title
        title_label = ttk.Label(
            self.frame,
            text="📋 Book Your Flight",
            font=("Helvetica", 20, "bold"),
            bootstyle="primary"
        )
        title_label.pack(pady=(0, 30))
        
        # Form frame
        form_frame = ttk.Frame(self.frame)
        form_frame.pack(fill="both", expand=True)
        
        # Passenger Name
        ttk.Label(form_frame, text="Passenger Name:", font=("Helvetica", 10, "bold")).pack(anchor="w", pady=(0, 5))
        self.name_entry = ttk.Entry(form_frame, width=40, font=("Helvetica", 10))
        self.name_entry.pack(fill="x", pady=(0, 15))
        
        # Flight Number
        ttk.Label(form_frame, text="Flight Number:", font=("Helvetica", 10, "bold")).pack(anchor="w", pady=(0, 5))
        self.flight_number_entry = ttk.Entry(form_frame, width=40, font=("Helvetica", 10))
        self.flight_number_entry.pack(fill="x", pady=(0, 15))
        
        # Departure
        ttk.Label(form_frame, text="Departure City:", font=("Helvetica", 10, "bold")).pack(anchor="w", pady=(0, 5))
        self.departure_entry = ttk.Entry(form_frame, width=40, font=("Helvetica", 10))
        self.departure_entry.pack(fill="x", pady=(0, 15))
        
        # Destination
        ttk.Label(form_frame, text="Destination City:", font=("Helvetica", 10, "bold")).pack(anchor="w", pady=(0, 5))
        self.destination_entry = ttk.Entry(form_frame, width=40, font=("Helvetica", 10))
        self.destination_entry.pack(fill="x", pady=(0, 15))
        
        # Date
        ttk.Label(form_frame, text="Travel Date (YYYY-MM-DD):", font=("Helvetica", 10, "bold")).pack(anchor="w", pady=(0, 5))
        self.date_entry = ttk.Entry(form_frame, width=40, font=("Helvetica", 10))
        self.date_entry.pack(fill="x", pady=(0, 15))
        
        # Seat Number
        ttk.Label(form_frame, text="Seat Number:", font=("Helvetica", 10, "bold")).pack(anchor="w", pady=(0, 5))
        self.seat_number_entry = ttk.Entry(form_frame, width=40, font=("Helvetica", 10))
        self.seat_number_entry.pack(fill="x", pady=(0, 30))
        
        # Buttons frame
        buttons_frame = ttk.Frame(form_frame)
        buttons_frame.pack(pady=20)
        
        # Submit Button
        submit_button = ttk.Button(
            buttons_frame,
            text="✈️ Book Flight",
            command=self.book_flight,
            style="success.TButton",
            width=20
        )
        submit_button.pack(side="left", padx=(0, 10))
        
        # Back Button
        back_button = ttk.Button(
            buttons_frame,
            text="🔙 Back to Home",
            command=self.show_home_page,
            style="secondary.TButton",
            width=20
        )
        back_button.pack(side="left")
        
        # Clear Button
        clear_button = ttk.Button(
            buttons_frame,
            text="🗑️ Clear Form",
            command=self.clear_form,
            style="warning.TButton",
            width=20
        )
        clear_button.pack(side="left", padx=(10, 0))
    
    def book_flight(self):
        """Book a flight with the entered details"""
        # Get values from entries
        name = self.name_entry.get().strip()
        flight_number = self.flight_number_entry.get().strip()
        departure = self.departure_entry.get().strip()
        destination = self.destination_entry.get().strip()
        date = self.date_entry.get().strip()
        seat_number = self.seat_number_entry.get().strip()
        
        # Validate inputs
        if not all([name, flight_number, departure, destination, date, seat_number]):
            messagebox.showerror("Error", "Please fill in all fields!")
            return
        
        # Validate date format
        try:
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid date in YYYY-MM-DD format!")
            return
        
        # Add reservation to database
        if db.add_reservation(name, flight_number, departure, destination, date, seat_number):
            messagebox.showinfo("Success", f"Flight booked successfully!\n\nPassenger: {name}\nFlight: {flight_number}\nFrom: {departure}\nTo: {destination}\nDate: {date}\nSeat: {seat_number}")
            self.clear_form()
        else:
            messagebox.showerror("Error", "Failed to book flight. Please try again.")
    
    def clear_form(self):
        """Clear all form fields"""
        self.name_entry.delete(0, tk.END)
        self.flight_number_entry.delete(0, tk.END)
        self.departure_entry.delete(0, tk.END)
        self.destination_entry.delete(0, tk.END)
        self.date_entry.delete(0, tk.END)
        self.seat_number_entry.delete(0, tk.END)
    
    def show(self):
        """Show the booking page"""
        self.frame.pack(fill="both", expand=True)
    
    def hide(self):
        """Hide the booking page"""
        self.frame.pack_forget()