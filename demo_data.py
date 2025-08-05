#!/usr/bin/env python3
"""
Demo data script for Flight Reservation System
Populates the database with sample reservations for testing
"""

import sys
import os

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from database import db

def add_demo_data():
    """Add sample reservations to the database"""
    print("🎭 Adding Demo Data to Flight Reservation System")
    print("=" * 50)
    
    # Sample reservations
    demo_reservations = [
        {
            "name": "Alice Johnson",
            "flight_number": "AA123",
            "departure": "New York",
            "destination": "Los Angeles",
            "date": "2024-12-25",
            "seat_number": "12A"
        },
        {
            "name": "Bob Smith",
            "flight_number": "DL456",
            "departure": "Atlanta",
            "destination": "Seattle",
            "date": "2024-12-26",
            "seat_number": "8C"
        },
        {
            "name": "Carol Davis",
            "flight_number": "UA789",
            "departure": "Chicago",
            "destination": "Miami",
            "date": "2024-12-27",
            "seat_number": "15F"
        },
        {
            "name": "David Wilson",
            "flight_number": "SW321",
            "departure": "Dallas",
            "destination": "Las Vegas",
            "date": "2024-12-28",
            "seat_number": "22B"
        },
        {
            "name": "Emma Brown",
            "flight_number": "BA654",
            "departure": "London",
            "destination": "Paris",
            "date": "2024-12-29",
            "seat_number": "7A"
        },
        {
            "name": "Frank Miller",
            "flight_number": "LH987",
            "departure": "Frankfurt",
            "destination": "Berlin",
            "date": "2024-12-30",
            "seat_number": "11D"
        },
        {
            "name": "Grace Taylor",
            "flight_number": "AF147",
            "departure": "Paris",
            "destination": "Rome",
            "date": "2024-12-31",
            "seat_number": "9C"
        },
        {
            "name": "Henry Anderson",
            "flight_number": "KL258",
            "departure": "Amsterdam",
            "destination": "Barcelona",
            "date": "2025-01-01",
            "seat_number": "14E"
        }
    ]
    
    # Add each reservation
    for i, reservation in enumerate(demo_reservations, 1):
        print(f"Adding reservation {i}/{len(demo_reservations)}: {reservation['name']}")
        
        success = db.add_reservation(
            name=reservation["name"],
            flight_number=reservation["flight_number"],
            departure=reservation["departure"],
            destination=reservation["destination"],
            date=reservation["date"],
            seat_number=reservation["seat_number"]
        )
        
        if success:
            print(f"✅ Added: {reservation['name']} - {reservation['flight_number']}")
        else:
            print(f"❌ Failed to add: {reservation['name']}")
    
    # Display final count
    final_reservations = db.get_all_reservations()
    print(f"\n📊 Total reservations in database: {len(final_reservations)}")
    
    print("\n" + "=" * 50)
    print("🎉 Demo data added successfully!")
    print("\n💡 You can now run the application to see the sample reservations.")
    
    # Close database connection
    db.close_connection()

if __name__ == "__main__":
    add_demo_data()