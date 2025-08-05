import tkinter as tk
from tkinter import ttk, messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class HomePage:
    def __init__(self, parent, show_booking_page, show_reservations_page):
        self.parent = parent
        self.show_booking_page = show_booking_page
        self.show_reservations_page = show_reservations_page
        self.frame = None
        self.create_widgets()
    
    def create_widgets(self):
        """Create the home page widgets"""
        # Main frame
        self.frame = ttk.Frame(self.parent, padding="20")
        
        # Title
        title_label = ttk.Label(
            self.frame, 
            text="✈️ Flight Reservation System", 
            font=("Helvetica", 24, "bold"),
            bootstyle="primary"
        )
        title_label.pack(pady=(0, 30))
        
        # Subtitle
        subtitle_label = ttk.Label(
            self.frame,
            text="Welcome to your flight booking portal",
            font=("Helvetica", 12),
            bootstyle="secondary"
        )
        subtitle_label.pack(pady=(0, 40))
        
        # Buttons frame
        buttons_frame = ttk.Frame(self.frame)
        buttons_frame.pack(expand=True)
        
        # Book Flight Button
        book_button = ttk.Button(
            buttons_frame,
            text="📋 Book Flight",
            command=self.show_booking_page,
            style="success.TButton",
            width=25
        )
        book_button.pack(pady=10)
        
        # View Reservations Button
        view_button = ttk.Button(
            buttons_frame,
            text="👁️ View Reservations",
            command=self.show_reservations_page,
            style="info.TButton",
            width=25
        )
        view_button.pack(pady=10)
        
        # Exit Button
        exit_button = ttk.Button(
            buttons_frame,
            text="🚪 Exit",
            command=self.exit_application,
            style="danger.TButton",
            width=25
        )
        exit_button.pack(pady=10)
        
        # Footer
        footer_label = ttk.Label(
            self.frame,
            text="© 2024 Flight Reservation System",
            font=("Helvetica", 8),
            bootstyle="secondary"
        )
        footer_label.pack(side="bottom", pady=20)
    
    def show(self):
        """Show the home page"""
        self.frame.pack(fill="both", expand=True)
    
    def hide(self):
        """Hide the home page"""
        self.frame.pack_forget()
    
    def exit_application(self):
        """Exit the application"""
        if messagebox.askokcancel("Exit", "Are you sure you want to exit?"):
            self.parent.quit()