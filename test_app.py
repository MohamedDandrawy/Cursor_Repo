#!/usr/bin/env python3
"""
Test script for Flight Reservation System
"""

import sys
import os

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from database import db

def test_database_operations():
    """Test basic database operations"""
    print("🧪 Testing Flight Reservation System Database Operations")
    print("=" * 50)
    
    # Test 1: Add a reservation
    print("\n1. Testing Add Reservation...")
    success = db.add_reservation(
        name="John Doe",
        flight_number="AA123",
        departure="New York",
        destination="Los Angeles",
        date="2024-12-25",
        seat_number="12A"
    )
    print(f"✅ Add reservation: {'SUCCESS' if success else 'FAILED'}")
    
    # Test 2: Get all reservations
    print("\n2. Testing Get All Reservations...")
    reservations = db.get_all_reservations()
    print(f"✅ Found {len(reservations)} reservations")
    for reservation in reservations:
        print(f"   - ID: {reservation[0]}, Name: {reservation[1]}, Flight: {reservation[2]}")
    
    # Test 3: Get specific reservation
    if reservations:
        print("\n3. Testing Get Specific Reservation...")
        reservation = db.get_reservation_by_id(reservations[0][0])
        if reservation:
            print(f"✅ Found reservation: {reservation[1]} on flight {reservation[2]}")
        else:
            print("❌ Failed to get specific reservation")
    
    # Test 4: Update reservation
    if reservations:
        print("\n4. Testing Update Reservation...")
        success = db.update_reservation(
            reservation_id=reservations[0][0],
            name="John Doe Updated",
            flight_number="AA123",
            departure="New York",
            destination="Los Angeles",
            date="2024-12-25",
            seat_number="15B"
        )
        print(f"✅ Update reservation: {'SUCCESS' if success else 'FAILED'}")
    
    # Test 5: Delete reservation
    if reservations:
        print("\n5. Testing Delete Reservation...")
        success = db.delete_reservation(reservations[0][0])
        print(f"✅ Delete reservation: {'SUCCESS' if success else 'FAILED'}")
    
    # Final check
    print("\n6. Final Reservation Count...")
    final_reservations = db.get_all_reservations()
    print(f"✅ Final count: {len(final_reservations)} reservations")
    
    print("\n" + "=" * 50)
    print("🎉 Database tests completed!")
    
    # Close database connection
    db.close_connection()

if __name__ == "__main__":
    test_database_operations()