import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from database import db
from home import HomePage
from booking import BookingPage
from reservations import ReservationsPage
from edit_reservation import EditReservationPage

class FlightReservationApp:
    def __init__(self):
        # Create the main window
        self.root = ttk.Window(
            title="Flight Reservation System",
            themename="cosmo",
            size=(800, 600),
            resizable=(True, True)
        )
        
        # Center the window
        self.center_window()
        
        # Initialize pages
        self.current_page = None
        self.pages = {}
        
        # Create pages
        self.create_pages()
        
        # Show home page initially
        self.show_home_page()
        
        # Bind window close event
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
    
    def center_window(self):
        """Center the window on the screen"""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f"{width}x{height}+{x}+{y}")
    
    def create_pages(self):
        """Create all application pages"""
        # Create pages with navigation callbacks
        self.pages['home'] = HomePage(
            self.root,
            self.show_booking_page,
            self.show_reservations_page
        )
        
        self.pages['booking'] = BookingPage(
            self.root,
            self.show_home_page
        )
        
        self.pages['reservations'] = ReservationsPage(
            self.root,
            self.show_home_page,
            self.show_edit_page
        )
        
        self.pages['edit'] = EditReservationPage(
            self.root,
            self.show_home_page,
            self.show_reservations_page
        )
    
    def hide_current_page(self):
        """Hide the currently displayed page"""
        if self.current_page and self.current_page in self.pages:
            self.pages[self.current_page].hide()
    
    def show_home_page(self):
        """Show the home page"""
        self.hide_current_page()
        self.pages['home'].show()
        self.current_page = 'home'
        self.root.title("Flight Reservation System - Home")
    
    def show_booking_page(self):
        """Show the booking page"""
        self.hide_current_page()
        self.pages['booking'].show()
        self.current_page = 'booking'
        self.root.title("Flight Reservation System - Book Flight")
    
    def show_reservations_page(self):
        """Show the reservations page"""
        self.hide_current_page()
        self.pages['reservations'].show()
        self.current_page = 'reservations'
        self.root.title("Flight Reservation System - View Reservations")
    
    def show_edit_page(self, reservation_id=None):
        """Show the edit reservation page"""
        self.hide_current_page()
        self.pages['edit'].show()
        if reservation_id:
            self.pages['edit'].load_reservation(reservation_id)
        self.current_page = 'edit'
        self.root.title("Flight Reservation System - Edit Reservation")
    
    def on_closing(self):
        """Handle application closing"""
        try:
            # Close database connection
            db.close_connection()
            print("Database connection closed")
        except:
            pass
        
        # Destroy the window
        self.root.destroy()
    
    def run(self):
        """Start the application"""
        try:
            self.root.mainloop()
        except KeyboardInterrupt:
            print("Application interrupted by user")
        except Exception as e:
            print(f"Application error: {e}")
        finally:
            self.on_closing()

def main():
    """Main function to start the application"""
    print("Starting Flight Reservation System...")
    app = FlightReservationApp()
    app.run()

if __name__ == "__main__":
    main()