import os
import colorama
from colorama import Fore, Style
from stack import Stack

colorama.init(autoreset=True)

class CustomerMenu:
    def __init__(self, stacks):
        self.stacks = stacks

    def clear_screen(self):
        os.system('cls')

    def show_menu(self):
        pilihan_item = {
            "1": "Cheetos",
            "2": "Coca Cola",
            "3": "Snickers"
        }

        while True:
            self.clear_screen()
            print(Fore.LIGHTRED_EX + "="*40)
            print(Fore.LIGHTRED_EX + " " * 13 + "MENU KONSUMEN")
            print(Fore.GREEN + "="*40)
            print(Fore.YELLOW + "1. Beli Item")
            print(Fore.YELLOW + "2. Menu Pemilik")
            print(Fore.YELLOW + "3. Keluar")
            print(Fore.GREEN + "="*40)
            pilihan = input("Masukkan pilihan Anda: ")

            if pilihan == "1":
                self.clear_screen()
                print(Fore.GREEN + "="*40)
                print(Fore.GREEN + " " * 10 + "PILIH ITEM YANG INGIN DIBELI")
                print(Fore.GREEN + "="*40)
                for key, item in pilihan_item.items():
                    if not self.stacks[item].is_empty():
                        harga = self.stacks[item].peek()["price"]
                        print(Fore.CYAN + f"{key}. {item} - Harga: Rp.{harga}")
                    else:
                        print(Fore.RED + f"{key}. {item} - (Kosong)")
                print(Fore.GREEN + "="*40)
                item_dipilih = input("Masukkan angka yang sesuai dengan item: ")

                if item_dipilih in pilihan_item:
                    item = pilihan_item[item_dipilih]
                    stack = self.stacks[item]
                    if stack.is_empty():
                        print(Fore.RED + f"\nMaaf, {item} sedang kosong. Silakan pilih item lain.")
                    else:
                        harga_item = stack.peek()["price"]
                        print(Fore.CYAN + f"\nHarga {item}: Rp.{harga_item}")
                        jumlah_beli = int(input(Fore.CYAN + f"Masukkan jumlah {item} yang ingin dibeli: "))

                        if jumlah_beli <= stack.count_item():
                            total_harga_item = harga_item * jumlah_beli
                            print(Fore.CYAN + f"\nTotal harga untuk {jumlah_beli} {item}: Rp.{total_harga_item}")
                            while True:
                                uang_bayar = float(input(Fore.CYAN + "Masukkan jumlah uang Anda: Rp. "))
                                if uang_bayar < total_harga_item:
                                    print(Fore.RED + "\nUang Anda tidak mencukupi. Silakan masukkan uang yang cukup.")
                                else:
                                    if uang_bayar == total_harga_item:
                                        print(Fore.GREEN + "\nTerima kasih! Pembayaran Anda sudah sesuai. Silakan ambil barang Anda.")
                                    else:
                                        print(Fore.GREEN + f"\nTerima kasih! Pembayaran Anda sudah sesuai. Silakan ambil barang Anda dan tunggu kembalian sebesar Rp.{uang_bayar - total_harga_item}.")
                                    break
                            for _ in range(jumlah_beli):
                                stack.pop()
                        else:
                            print(Fore.RED + f"\nJumlah {item} yang diminta tidak tersedia. Tersedia hanya {stack.count_item()} {item}.")
                else:
                    print(Fore.RED + "\nPilihan item tidak valid. Silakan masukkan angka 1, 2, atau 3.")
            elif pilihan == "2":
                return "owner"
            elif pilihan == "3":
                break
            else:
                print(Fore.RED + "\nPilihan tidak valid. Silakan coba lagi.")
            input(Fore.CYAN + "\nTekan Enter untuk melanjutkan...")
