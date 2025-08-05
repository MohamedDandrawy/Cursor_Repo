# Flight Reservation System

A modern desktop application for managing flight reservations built with Python, Tkinter, and SQLite.

## ✈️ Features

- **Book Flights**: Create new flight reservations with passenger details
- **View Reservations**: Display all reservations in a searchable table
- **Edit Reservations**: Update existing reservation details
- **Delete Reservations**: Remove reservations with confirmation
- **Search Functionality**: Search reservations by passenger name, flight number, or cities
- **Modern UI**: Beautiful interface using ttkbootstrap theme
- **Database Storage**: SQLite database for persistent data storage

## 🛠️ Technologies Used

- **Python 3.8+**
- **Tkinter** - GUI framework
- **ttkbootstrap** - Modern UI components
- **SQLite** - Database management
- **PyInstaller** - Executable creation

## 📋 Requirements

- Python 3.8 or higher
- pip (Python package installer)

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd flight_reservation_app
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python main.py
   ```

## 📁 Project Structure

```
flight_reservation_app/
├── main.py                 # Main application entry point
├── database.py            # SQLite database connection and operations
├── home.py               # Home page UI
├── booking.py            # Flight booking form
├── reservations.py       # View all reservations
├── edit_reservation.py   # Edit/Update reservation functionality
├── flights.db            # SQLite database file
├── requirements.txt      # Python dependencies
├── README.md            # Project documentation
└── .gitignore          # Git ignore file
```

## 🎯 Usage Guide

### 1. Home Page
- **Book Flight**: Navigate to the booking form
- **View Reservations**: See all existing reservations
- **Exit**: Close the application

### 2. Booking a Flight
1. Click "📋 Book Flight" from the home page
2. Fill in all required fields:
   - Passenger Name
   - Flight Number
   - Departure City
   - Destination City
   - Travel Date (YYYY-MM-DD format)
   - Seat Number
3. Click "✈️ Book Flight" to save
4. Use "🗑️ Clear Form" to reset fields
5. Use "🔙 Back to Home" to return

### 3. Viewing Reservations
1. Click "👁️ View Reservations" from the home page
2. All reservations are displayed in a table
3. Use the search box to filter reservations
4. Click "🔄 Refresh" to reload data
5. Select a reservation and click:
   - "✏️ Edit Selected" to modify
   - "🗑️ Delete Selected" to remove

### 4. Editing Reservations
1. Select a reservation from the list
2. Click "✏️ Edit Selected"
3. Modify the pre-filled form
4. Click "💾 Update Reservation" to save changes
5. Use navigation buttons to return

## 🗄️ Database Schema

The application uses SQLite with the following table structure:

```sql
CREATE TABLE reservations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    flight_number TEXT NOT NULL,
    departure TEXT NOT NULL,
    destination TEXT NOT NULL,
    date TEXT NOT NULL,
    seat_number TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## 🏗️ Building Executable

To create a standalone executable:

1. **Install PyInstaller**
   ```bash
   pip install pyinstaller
   ```

2. **Build the executable**
   ```bash
   pyinstaller --onefile --windowed main.py
   ```

3. **Find the executable**
   - Windows: `dist/main.exe`
   - Linux: `dist/main`
   - macOS: `dist/main`

## 🐛 Troubleshooting

### Common Issues

1. **Import Error for ttkbootstrap**
   ```bash
   pip install ttkbootstrap==1.10.1
   ```

2. **Database Connection Error**
   - Ensure write permissions in the application directory
   - Check if `flights.db` is not locked by another process

3. **GUI Not Displaying Properly**
   - Update your Python version to 3.8+
   - Ensure ttkbootstrap is properly installed

### Error Messages

- **"Please fill in all fields"**: Complete all form fields
- **"Invalid date format"**: Use YYYY-MM-DD format for dates
- **"Reservation not found"**: The selected reservation may have been deleted

## 🔧 Development

### Adding New Features

1. **New Pages**: Create new page classes following the existing pattern
2. **Database Operations**: Add methods to `database.py`
3. **UI Components**: Use ttkbootstrap for consistent styling

### Code Structure

- **Page Classes**: Each page is a separate class with show/hide methods
- **Database Class**: Centralized database operations
- **Main App**: Manages navigation between pages

## 📝 License

This project is open source and available under the MIT License.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📞 Support

For issues and questions:
- Create an issue in the repository
- Check the troubleshooting section above
- Ensure all dependencies are installed

## 🎉 Acknowledgments

- ttkbootstrap for the beautiful UI components
- SQLite for reliable data storage
- Python community for excellent documentation

---

**Happy Flying! ✈️**