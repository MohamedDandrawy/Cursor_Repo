import tkinter as tk
from tkinter import ttk, messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from datetime import datetime
from database import db

class EditReservationPage:
    def __init__(self, parent, show_home_page, show_reservations_page):
        self.parent = parent
        self.show_home_page = show_home_page
        self.show_reservations_page = show_reservations_page
        self.frame = None
        self.reservation_id = None
        self.create_widgets()
    
    def create_widgets(self):
        """Create the edit reservation page widgets"""
        # Main frame
        self.frame = ttk.Frame(self.parent, padding="20")
        
        # Title
        self.title_label = ttk.Label(
            self.frame,
            text="✏️ Edit Reservation",
            font=("Helvetica", 20, "bold"),
            bootstyle="primary"
        )
        self.title_label.pack(pady=(0, 30))
        
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
        
        # Update Button
        update_button = ttk.Button(
            buttons_frame,
            text="💾 Update Reservation",
            command=self.update_reservation,
            style="success.TButton",
            width=20
        )
        update_button.pack(side="left", padx=(0, 10))
        
        # Back Button
        back_button = ttk.Button(
            buttons_frame,
            text="🔙 Back to Reservations",
            command=self.show_reservations_page,
            style="secondary.TButton",
            width=20
        )
        back_button.pack(side="left", padx=(0, 10))
        
        # Home Button
        home_button = ttk.Button(
            buttons_frame,
            text="🏠 Back to Home",
            command=self.show_home_page,
            style="info.TButton",
            width=20
        )
        home_button.pack(side="left")
        
        # Status label
        self.status_label = ttk.Label(
            self.frame,
            text="",
            font=("Helvetica", 9),
            bootstyle="secondary"
        )
        self.status_label.pack(pady=(10, 0))
    
    def load_reservation(self, reservation_id):
        """Load reservation data into the form"""
        self.reservation_id = reservation_id
        reservation = db.get_reservation_by_id(reservation_id)
        
        if reservation:
            # Clear existing entries
            self.name_entry.delete(0, tk.END)
            self.flight_number_entry.delete(0, tk.END)
            self.departure_entry.delete(0, tk.END)
            self.destination_entry.delete(0, tk.END)
            self.date_entry.delete(0, tk.END)
            self.seat_number_entry.delete(0, tk.END)
            
            # Fill with reservation data
            self.name_entry.insert(0, reservation[1])  # name
            self.flight_number_entry.insert(0, reservation[2])  # flight_number
            self.departure_entry.insert(0, reservation[3])  # departure
            self.destination_entry.insert(0, reservation[4])  # destination
            self.date_entry.insert(0, reservation[5])  # date
            self.seat_number_entry.insert(0, reservation[6])  # seat_number
            
            # Update title
            self.title_label.config(text=f"✏️ Edit Reservation - {reservation[1]}")
            self.status_label.config(text=f"Editing reservation ID: {reservation_id}")
        else:
            messagebox.showerror("Error", "Reservation not found!")
            self.show_reservations_page()
    
    def update_reservation(self):
        """Update the reservation with new data"""
        if not self.reservation_id:
            messagebox.showerror("Error", "No reservation selected!")
            return
        
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
        
        # Update reservation in database
        if db.update_reservation(self.reservation_id, name, flight_number, departure, destination, date, seat_number):
            messagebox.showinfo("Success", f"Reservation updated successfully!\n\nPassenger: {name}\nFlight: {flight_number}\nFrom: {departure}\nTo: {destination}\nDate: {date}\nSeat: {seat_number}")
            self.show_reservations_page()
        else:
            messagebox.showerror("Error", "Failed to update reservation. Please try again.")
    
    def show(self):
        """Show the edit reservation page"""
        self.frame.pack(fill="both", expand=True)
    
    def hide(self):
        """Hide the edit reservation page"""
        self.frame.pack_forget()