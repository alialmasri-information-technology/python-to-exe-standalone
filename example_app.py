# example_app.py

import time

def main():
    print("--- PyInstaller Example Application ---")
    print("This is a simple Python script that will be converted into a standalone executable.")
    print("The current time is:", time.ctime())
    
    # This line is important to keep the console window open on Windows executables
    # so the user can read the output before it closes.
    input("\nPress Enter to close the application...")

if __name__ == "__main__":
    main()
