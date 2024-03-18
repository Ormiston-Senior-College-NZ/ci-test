def main():
    if platform.system() == 'Windows':
        print("This is a Windows-specific functionality.")
        raise Exception("This script is intentionally failing on Windows.")
    else:
        # Intentionally raising an exception on macOS
        raise OSError("This script is not compatible with macOS.")
        print("This script works on", platform.system())

if __name__ == "__main__":
    main()
