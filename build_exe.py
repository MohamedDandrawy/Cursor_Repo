#!/usr/bin/env python3
"""
Build script for Flight Reservation System
Creates a standalone executable using PyInstaller
"""

import os
import sys
import subprocess
import shutil

def install_pyinstaller():
    """Install PyInstaller if not already installed"""
    try:
        import PyInstaller
        print("✅ PyInstaller is already installed")
    except ImportError:
        print("📦 Installing PyInstaller...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
        print("✅ PyInstaller installed successfully")

def clean_build_dirs():
    """Clean previous build directories"""
    dirs_to_clean = ["build", "dist", "__pycache__"]
    for dir_name in dirs_to_clean:
        if os.path.exists(dir_name):
            print(f"🧹 Cleaning {dir_name}...")
            shutil.rmtree(dir_name)
    
    # Clean .spec files
    for file in os.listdir("."):
        if file.endswith(".spec"):
            print(f"🧹 Removing {file}...")
            os.remove(file)

def build_executable():
    """Build the executable using PyInstaller"""
    print("🔨 Building executable...")
    
    # PyInstaller command
    cmd = [
        "pyinstaller",
        "--onefile",           # Create a single executable file
        "--windowed",          # Hide console window (Windows)
        "--name=FlightReservationSystem",  # Name of the executable
        "--add-data=flights.db;.",  # Include database file
        "main.py"
    ]
    
    try:
        subprocess.check_call(cmd)
        print("✅ Executable built successfully!")
        
        # Check if executable was created
        exe_path = os.path.join("dist", "FlightReservationSystem.exe")
        if os.path.exists(exe_path):
            print(f"📁 Executable location: {exe_path}")
            print(f"📏 File size: {os.path.getsize(exe_path) / (1024*1024):.1f} MB")
        else:
            print("⚠️  Executable not found in expected location")
            
    except subprocess.CalledProcessError as e:
        print(f"❌ Build failed: {e}")
        return False
    
    return True

def create_installer_script():
    """Create a simple installer script"""
    installer_content = """@echo off
echo Installing Flight Reservation System...
echo.
echo This will create a desktop shortcut and start menu entry.
echo.
pause

REM Create desktop shortcut
powershell "$WshShell = New-Object -comObject WScript.Shell; $Shortcut = $WshShell.CreateShortcut('%USERPROFILE%\\Desktop\\Flight Reservation System.lnk'); $Shortcut.TargetPath = '%~dp0FlightReservationSystem.exe'; $Shortcut.Save()"

echo.
echo Installation completed!
echo You can now run the application from your desktop.
pause
"""
    
    with open("install.bat", "w") as f:
        f.write(installer_content)
    print("✅ Created installer script: install.bat")

def main():
    """Main build process"""
    print("🚀 Flight Reservation System - Build Process")
    print("=" * 50)
    
    # Check if we're in the right directory
    if not os.path.exists("main.py"):
        print("❌ Error: main.py not found. Please run this script from the project directory.")
        return
    
    # Install PyInstaller
    install_pyinstaller()
    
    # Clean previous builds
    clean_build_dirs()
    
    # Build executable
    if build_executable():
        # Create installer script
        create_installer_script()
        
        print("\n" + "=" * 50)
        print("🎉 Build process completed successfully!")
        print("\n📋 Next steps:")
        print("1. Test the executable: dist/FlightReservationSystem.exe")
        print("2. Distribute the executable and database file")
        print("3. Use install.bat for easy installation")
        
        # List files in dist directory
        if os.path.exists("dist"):
            print("\n📁 Files in dist directory:")
            for file in os.listdir("dist"):
                file_path = os.path.join("dist", file)
                size = os.path.getsize(file_path) / (1024*1024)
                print(f"   - {file} ({size:.1f} MB)")
    else:
        print("❌ Build process failed!")

if __name__ == "__main__":
    main()