import platform

def main():
    if platform.system() == 'Windows':
        print("This is a Windows-specific functionality.")
    else:
        # Intentionally raising an exception on macOS
        raise OSError("This script is not compatible with macOS.")

if __name__ == "__main__":
    main()
