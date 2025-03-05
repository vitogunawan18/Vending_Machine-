import os
import msvcrt

class Log:
    def __init__(self):
        self.correct_username = "vito"
        self.correct_password = "12345"

    def login(self):
        print("="*30)
        print("      LOGIN SYSTEM      ")
        print("="*30)

        # Meminta input username
        username = input("Username: ")

        # Meminta input password
        print("Password: ", end='', flush=True)
        password = ""
        while True:
            key = msvcrt.getch()
            key = key.decode('utf-8')

            if key == '\r':  # Enter key
                print('')
                break
            elif key == '\b':  # Backspace key
                if password:
                    password = password[:-1]
                    print('\b \b', end='', flush=True)
            else:
                password += key
                print('*', end='', flush=True)

        # Memeriksa kecocokan username dan password
        if username == self.correct_username and password == self.correct_password:
            print("\nLogin successful! Welcome, Vito!")
            return True
        else:
            print("\nLogin failed! Invalid username or password.")
            return False
