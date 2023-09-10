# Import modul yang diperlukan
from transaction import Transaction  # Import class Transaction dari modul transaction
import datetime
import time

# Fungsi untuk membersihkan layar konsol
def clear_screen():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

# Fungsi untuk mendapatkan informasi transaksi dari pengguna
def get_transaction_info():
    transaction_id = input("Masukkan ID transaksi: ")  # Meminta ID transaksi dari pengguna
    clear_screen()
    while True:
        transaction_date = input("Masukkan tanggal transaksi (YYYY-MM-DD): ")  # Meminta tanggal transaksi dari pengguna
        try:
            transaction_date = datetime.datetime.strptime(transaction_date, "%Y-%m-%d").date()  # Mengonversi tanggal ke dalam format yang benar
            return transaction_id, transaction_date  # Mengembalikan ID transaksi dan tanggal transaksi
        except ValueError:
            print("Format tanggal tidak valid. Gunakan format YYYY-MM-DD.")
            time.sleep(1)  # Menunggu 1 detik sebelum membersihkan layar
            clear_screen()

# Fungsi untuk menampilkan isi keranjang belanja
def display_cart(transaction):
    cart = transaction.get_cart()
    if not cart:
        print("Keranjang kosong.")
        print("===================== Keranjang Belanja =====================")
        print(f"|{'Nama Item':<20}|{'Jumlah':<10}|{'Harga/Item':<15}|{'Total Harga'}|")
    else:
        clear_screen()
        print("====================== Kasir Toko  ==========================")
        print(f"ID Transaksi: {transaction_id}")
        print(f"Tanggal Transaksi: {transaction_date.strftime('%Y-%m-%d')}")
        print("===================== Keranjang Belanja =====================")
        print(f"|{'Nama Item':<20}|{'Jumlah':<10}|{'Harga/Item':<15}|{'Total Harga'}|")
        for item in cart:
            name = f"{item['name']:<20}"
            quantity = f"{item['quantity']:<10}"
            price_per_item = f"Rp {item['price']:.2f}"  # Mengganti simbol mata uang dari $ ke Rp (rupiah)
            total_price = f"Rp {item['quantity'] * item['price']:.2f}"  # Mengganti simbol mata uang dari $ ke Rp (rupiah)
            print(f"|{name}|{quantity}|{price_per_item:<15}|{total_price} |")

# Bagian utama program
if __name__ == "__main__":
    while True:
        clear_screen()
        print("====================== Kasir Toko  ==========================")
        transaction_id, transaction_date = get_transaction_info()  # Mendapatkan informasi transaksi dari pengguna
        if transaction_id is None:
            exit(1)

        transaction = Transaction()

        while True:
            clear_screen()
            print("====================== Kasir Toko  ==========================")
            print(f"ID Transaksi: {transaction_id}")
            print(f"Tanggal Transaksi: {transaction_date.strftime('%Y-%m-%d')}")
            print("\n", (" "))
            display_cart(transaction)
            print("=============================================================")
            print(f"Total Harga: Rp {transaction.calculate_total_price():.2f}")  # Mengganti simbol mata uang dari $ ke Rp (rupiah)
            print("\n1. Tambah Item")
            print("2. Update Item")
            print("3. Hapus Item")
            print("4. Reset Transaksi")
            print("5. Selesai Transaksi")
            print("Pilihan Anda: ")

            choice = input()

            if choice == "1":
                clear_screen()
                name = input("Masukkan nama item: ")
                quantity = int(input("Masukkan jumlah item: "))
                price = float(input("Masukkan harga per item: "))
                transaction.add_item(name, quantity, price)  # Menambahkan item ke keranjang
            elif choice == "2":
                display_cart(transaction)
                name = input("Masukkan nama item yang ingin diupdate: ")
                update_type = input("Apa yang ingin Anda update (nama/jumlah/harga): ").lower()
                if update_type == "nama":
                    new_name = input("Masukkan nama baru: ")
                    transaction.update_item_name(name, new_name)  # Mengupdate nama item
                elif update_type == "jumlah":
                    new_quantity = int(input("Masukkan jumlah baru: "))
                    transaction.update_item_quantity(name, new_quantity)  # Mengupdate jumlah item
                elif update_type == "harga":
                    new_price = float(input("Masukkan harga baru: "))
                    transaction.update_item_price(name, new_price)  # Mengupdate harga item
                else:
                    print("Pilihan tidak valid.")
            elif choice == "3":
                display_cart(transaction)
                name = input("Masukkan nama item yang ingin dihapus: ")
                transaction.delete_item(name)  # Menghapus item dari keranjang
            elif choice == "4":
                transaction.reset_transaction()  # Mengatur ulang transaksi
            elif choice == "5":
                while True:
                    clear_screen()
                    print("====================== Kasir Toko  ==========================")
                    print(f"ID Transaksi: {transaction_id}")
                    print(f"Tanggal Transaksi: {transaction_date.strftime('%Y-%m-%d')}")
                    print("\n")
                    display_cart(transaction)
                    total_price = transaction.calculate_total_price()
                    discount_price = transaction.apply_discount()
                    print(f"Total Harga (tanpa diskon): Rp {total_price:.2f}")  # Mengganti simbol mata uang dari $ ke Rp (rupiah)
                    print(f"Total Harga (diskon): Rp {discount_price:.2f}")  # Mengganti simbol mata uang dari $ ke Rp (rupiah)
                    print("\n1. Kembali ke Transaksi Sebelumnya")
                    print("2. Lanjut ke Pembayaran")
                    print("Pilihan Anda: ")

                    choice = input()

                    if choice == "1":
                        break
                    elif choice == "2":
                        clear_screen()
                        print("====================== Kasir Toko  ==========================")
                        print(f"ID Transaksi: {transaction_id}")
                        print(f"Tanggal Transaksi: {transaction_date.strftime('%Y-%m-%d')}")
                        print("\n")
                        display_cart(transaction)
                        print(f"Total Harga (tanpa diskon): Rp {total_price:.2f}")  # Mengganti simbol mata uang dari $ ke Rp (rupiah)
                        print(f"Total Harga (diskon): Rp {discount_price:.2f}")  # Mengganti simbol mata uang dari $ ke Rp (rupiah)
                        payment = float(input("Total Pembayaran: Rp "))  # Mengganti simbol mata uang dari $ ke Rp (rupiah)

                        while payment < discount_price:
                            print("Pembayaran kurang. Uang yang Anda masukkan tidak mencukupi.")
                            payment = float(input("Total Pembayaran: Rp "))  # Mengganti simbol mata uang dari $ ke Rp (rupiah)

                        change = payment - discount_price
                        print(f"Kembalian: Rp {change:.2f}")  # Mengganti simbol mata uang dari $ ke Rp (rupiah)
                        input("Tekan Enter untuk melanjutkan...")
                        clear_screen()
                        exit(0)
                    else:
                        print("Pilihan tidak valid. Silakan coba lagi.")

            else:
                print("Pilihan tidak valid. Silakan coba lagi.")
        break
