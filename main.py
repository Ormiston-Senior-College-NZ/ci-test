try:
    import winreg  # Attempt to import a Windows-specific module
except ImportError:
    print("This script can't run on macOS.")
