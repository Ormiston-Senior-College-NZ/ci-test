import platform

def main():
    if platform.system() == 'Windows':
        raise Exception("This script is intentionally failing on Windows.")
    else:
        print("This script works on", platform.system())

if __name__ == "__main__":
    main()
