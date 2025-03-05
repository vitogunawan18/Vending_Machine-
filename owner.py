from datetime import datetime
import os
import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)

class OwnerMenu:
    def __init__(self, stacks):
        self.stacks = stacks

    def clear_screen(self):
        os.system('cls')

    def print_header(self, title):
        print(Fore.GREEN + "="*40)
        print(Fore.GREEN + f"{' ' * ((40 - len(title)) // 2)}{title}")
        print(Fore.GREEN + "="*40)

    def print_table(self, headers, rows):
    # Menghitung lebar maksimum untuk setiap kolom
        lebar_kolom = [max(len(str(item)) for item in col) for col in zip(headers, *rows)]
    # Membuat baris header
        baris_header = " | ".join(f"{header.ljust(lebar)}" for header, lebar in zip(headers, lebar_kolom))
    # Membuat baris pemisah
        pemisah = "-+-".join("-" * lebar for lebar in lebar_kolom)
    # Mencetak header dengan warna teks biru
        print(Fore.BLUE + baris_header)
        print(Fore.BLUE + pemisah)
    # Mencetak setiap baris data dengan warna teks biru
        for baris in baris_data:
            print(Fore.BLUE + " | ".join(f"{str(item).ljust(lebar)}" for item, lebar in zip(baris, lebar_kolom)))

    def show_menu(self):
        batas_maksimal = {
            "Cheetos": {"limit": 5, "price": 7000},
            "Coca Cola": {"limit": 5, "price": 5000},
            "Snickers": {"limit": 5, "price": 3000}
        }

        pilihan_item = {
            "1": "Cheetos",
            "2": "Coca Cola",
            "3": "Snickers"
        }

        while True:
            self.clear_screen()
            self.print_header("MENU OWNER")
            print(Fore.YELLOW + "1. Menambah Item (restock)")
            print(Fore.YELLOW + "2. Mengambil Item (Pop)")
            print(Fore.YELLOW + "3. Lihat Stok Saat Ini")
            print(Fore.YELLOW + "4. Keluar")
            print(Fore.GREEN + "="*40)
            pilihan = input("Masukkan pilihan Anda: ")

            if pilihan == "1":
                self.clear_screen()
                self.print_header("Pilih Item untuk Ditambahkan ke Vending Machine")
                print(Fore.YELLOW + "1. Cheetos")
                print(Fore.YELLOW + "2. Coca Cola")
                print(Fore.YELLOW + "3. Snickers")
                print(Fore.GREEN + "="*40)
                item_dipilih = input("Masukkan angka yang sesuai dengan item: ")
                self.clear_screen()
                if item_dipilih in pilihan_item:
                    item = pilihan_item[item_dipilih]
                    stack = self.stacks[item]
                    current_price = batas_maksimal[item]["price"]
                    print(f"Harga saat ini untuk {item} adalah Rp. {current_price}")
                    change_price = input(f"Apakah Anda ingin mengganti harga untuk {item}? (y/n): ").strip().lower()
                    if change_price == 'y':
                        while True:
                            try:
                                harga_item = int(input(f"Masukkan harga baru untuk {item}: Rp. "))
                                batas_maksimal[item]["price"] = harga_item
                                break
                            except ValueError:
                                print(Fore.RED + "Harga tidak valid. Masukkan angka.")
                    else:
                        harga_item = current_price
                    self.clear_screen()
                    jumlah_sekarang = stack.count_item()
                    if jumlah_sekarang < batas_maksimal[item]["limit"]:
                        max_tambah = batas_maksimal[item]["limit"] - jumlah_sekarang
                        print(f"Anda dapat menambahkan maksimal {max_tambah} {item}.")
                        while True:
                            try:
                                jumlah_tambah = int(input(f"Masukkan jumlah {item} yang ingin ditambahkan: "))
                                if 0 < jumlah_tambah <= max_tambah:
                                    break
                                else:
                                    print(Fore.RED + f"Jumlah tidak valid. Masukkan angka antara 1 dan {max_tambah}.")
                            except ValueError:
                                print(Fore.RED + "Jumlah tidak valid. Masukkan angka.")
                        for _ in range(jumlah_tambah):
                            while True:
                                expiry_date = input(f"Masukkan tanggal kadaluarsa untuk {item} (format DD-MM-YYYY): ")
                                try:
                                    expiry_date = datetime.strptime(expiry_date, "%d-%m-%Y").strftime('%Y-%m-%d')
                                    stack.push(item, expiry_date, harga_item)
                                    break
                                except ValueError:
                                    print(Fore.RED + "Format tanggal tidak valid. Silakan coba lagi.")
                        print(f"{jumlah_tambah} {item} telah ditambahkan ke Vending Machine.")
                    else:
                        print(Fore.RED + f"{item} telah mencapai batas maksimal ({batas_maksimal[item]['limit']}). Tidak dapat menambahkan lebih banyak.")
                else:
                    print(Fore.RED + "Pilihan item tidak valid. Silakan masukkan angka 1, 2, atau 3.")
            elif pilihan == "2":
                self.clear_screen()
                self.print_header("Pilih Item yang Ingin Diambil dari Vending Machine")
                print(Fore.YELLOW + "1. Cheetos")
                print(Fore.YELLOW + "2. Coca Cola")
                print(Fore.YELLOW + "3. Snickers")
                print(Fore.GREEN + "="*40)
                item_dipilih = input("Masukkan angka yang sesuai dengan item: ")

                if item_dipilih in pilihan_item:
                    item = pilihan_item[item_dipilih]
                    stack = self.stacks[item]
                    item_terambil = stack.pop()
                    if item_terambil != "Stock kosong":
                        item_name, expiry_date = item_terambil["item"], item_terambil["expiry_date"]
                        print(f"{item_name} (Kadaluarsa: {expiry_date}) telah diambil dari Vending Machine.")
                    else:
                        print(Fore.RED + item_terambil)
                else:
                    print(Fore.RED + "Pilihan item tidak valid. Silakan masukkan angka 1, 2, atau 3.")
            elif pilihan == "3":
                self.clear_screen()
                self.print_header("STOK SAAT INI")
                headers = ["Item", "Jumlah", "Kadaluarsa"]
                rows = []
                for item, stack in self.stacks.items():
                    count = stack.count_item()
                    if count > 0:
                        for itm, expiry in stack.get_all_items():
                            rows.append([item, itm, expiry])
                    else:
                        rows.append([item, "0", "-"])
                self.print_table(headers, rows)
            elif pilihan == "4":
                break
            else:
                print(Fore.RED + "Pilihan tidak valid. Silakan coba lagi.")
            input(Fore.CYAN + "Tekan Enter untuk melanjutkan...")

# Assuming Stack class exists with methods count_item(), push(), pop(), and get_all_items()
