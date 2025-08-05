import tkinter as tk
from tkinter import ttk, messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from database import db

class ReservationsPage:
    def __init__(self, parent, show_home_page, show_edit_page):
        self.parent = parent
        self.show_home_page = show_home_page
        self.show_edit_page = show_edit_page
        self.frame = None
        self.tree = None
        self.create_widgets()
        self.load_reservations()
    
    def create_widgets(self):
        """Create the reservations page widgets"""
        # Main frame
        self.frame = ttk.Frame(self.parent, padding="20")
        
        # Title
        title_label = ttk.Label(
            self.frame,
            text="👁️ View All Reservations",
            font=("Helvetica", 20, "bold"),
            bootstyle="primary"
        )
        title_label.pack(pady=(0, 20))
        
        # Search frame
        search_frame = ttk.Frame(self.frame)
        search_frame.pack(fill="x", pady=(0, 20))
        
        ttk.Label(search_frame, text="Search:", font=("Helvetica", 10, "bold")).pack(side="left", padx=(0, 10))
        self.search_entry = ttk.Entry(search_frame, width=30, font=("Helvetica", 10))
        self.search_entry.pack(side="left", padx=(0, 10))
        self.search_entry.bind('<KeyRelease>', self.search_reservations)
        
        refresh_button = ttk.Button(
            search_frame,
            text="🔄 Refresh",
            command=self.load_reservations,
            style="info.TButton"
        )
        refresh_button.pack(side="left")
        
        # Treeview frame
        tree_frame = ttk.Frame(self.frame)
        tree_frame.pack(fill="both", expand=True, pady=(0, 20))
        
        # Create Treeview
        columns = ("ID", "Name", "Flight Number", "Departure", "Destination", "Date", "Seat Number")
        self.tree = ttk.Treeview(tree_frame, columns=columns, show="headings", height=15)
        
        # Define headings
        self.tree.heading("ID", text="ID")
        self.tree.heading("Name", text="Passenger Name")
        self.tree.heading("Flight Number", text="Flight Number")
        self.tree.heading("Departure", text="Departure")
        self.tree.heading("Destination", text="Destination")
        self.tree.heading("Date", text="Date")
        self.tree.heading("Seat Number", text="Seat Number")
        
        # Define column widths
        self.tree.column("ID", width=50, anchor="center")
        self.tree.column("Name", width=150, anchor="w")
        self.tree.column("Flight Number", width=120, anchor="center")
        self.tree.column("Departure", width=100, anchor="center")
        self.tree.column("Destination", width=100, anchor="center")
        self.tree.column("Date", width=100, anchor="center")
        self.tree.column("Seat Number", width=100, anchor="center")
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        # Pack tree and scrollbar
        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Buttons frame
        buttons_frame = ttk.Frame(self.frame)
        buttons_frame.pack(pady=10)
        
        # Edit Button
        edit_button = ttk.Button(
            buttons_frame,
            text="✏️ Edit Selected",
            command=self.edit_selected,
            style="warning.TButton",
            width=15
        )
        edit_button.pack(side="left", padx=(0, 10))
        
        # Delete Button
        delete_button = ttk.Button(
            buttons_frame,
            text="🗑️ Delete Selected",
            command=self.delete_selected,
            style="danger.TButton",
            width=15
        )
        delete_button.pack(side="left", padx=(0, 10))
        
        # Back Button
        back_button = ttk.Button(
            buttons_frame,
            text="🔙 Back to Home",
            command=self.show_home_page,
            style="secondary.TButton",
            width=15
        )
        back_button.pack(side="left")
        
        # Status label
        self.status_label = ttk.Label(
            self.frame,
            text="",
            font=("Helvetica", 9),
            bootstyle="secondary"
        )
        self.status_label.pack(pady=(10, 0))
    
    def load_reservations(self):
        """Load all reservations from database"""
        # Clear existing items
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Get reservations from database
        reservations = db.get_all_reservations()
        
        # Add to treeview
        for reservation in reservations:
            self.tree.insert("", "end", values=reservation)
        
        # Update status
        self.status_label.config(text=f"Total Reservations: {len(reservations)}")
    
    def search_reservations(self, event=None):
        """Search reservations based on entered text"""
        search_term = self.search_entry.get().lower()
        
        # Clear existing items
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Get all reservations
        reservations = db.get_all_reservations()
        
        # Filter and add matching items
        for reservation in reservations:
            # Search in name, flight number, departure, destination
            if (search_term in str(reservation[1]).lower() or  # name
                search_term in str(reservation[2]).lower() or  # flight_number
                search_term in str(reservation[3]).lower() or  # departure
                search_term in str(reservation[4]).lower()):   # destination
                self.tree.insert("", "end", values=reservation)
    
    def edit_selected(self):
        """Edit the selected reservation"""
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "Please select a reservation to edit!")
            return
        
        # Get the selected reservation data
        reservation_data = self.tree.item(selected_item[0])['values']
        reservation_id = reservation_data[0]
        
        # Show edit page with the selected reservation
        self.show_edit_page(reservation_id)
    
    def delete_selected(self):
        """Delete the selected reservation"""
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "Please select a reservation to delete!")
            return
        
        # Get the selected reservation data
        reservation_data = self.tree.item(selected_item[0])['values']
        reservation_id = reservation_data[0]
        passenger_name = reservation_data[1]
        
        # Confirm deletion
        if messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete the reservation for {passenger_name}?"):
            if db.delete_reservation(reservation_id):
                messagebox.showinfo("Success", "Reservation deleted successfully!")
                self.load_reservations()
            else:
                messagebox.showerror("Error", "Failed to delete reservation!")
    
    def show(self):
        """Show the reservations page"""
        self.frame.pack(fill="both", expand=True)
        self.load_reservations()
    
    def hide(self):
        """Hide the reservations page"""
        self.frame.pack_forget()