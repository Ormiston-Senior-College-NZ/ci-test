import os

def main():
    if os.name == 'nt':  # Check if the operating system is Windows
        print("This is a Windows-specific functionality.")
    else:
        print("This functionality may not work on macOS.")

if __name__ == "__main__":
    main()
