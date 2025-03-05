from owner import OwnerMenu
from customer import CustomerMenu
from log import Log
from stack import Stack
import os

def clear_screen():
    os.system('cls')

if __name__ == "__main__":
    stacks = {
        "Cheetos": Stack(),
        "Coca Cola": Stack(),
        "Snickers": Stack()
    }
    log_instance = Log()
    customer_menu = CustomerMenu(stacks)

    while True:
        clear_screen()
        menu_result = customer_menu.show_menu()

        if menu_result == "owner":
            clear_screen()
            if log_instance.login():
                owner_menu = OwnerMenu(stacks)
                owner_menu.show_menu()
            else:
                print("Username atau password salah.")
                input("Tekan Enter untuk melanjutkan...")
        else:
            break
