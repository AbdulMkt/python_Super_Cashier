# Super Cashier System

Program yang didefinisikan adalah sebuah sistem kasir self-service yang dibuat oleh Andi, pemilik sebuah supermarket besar di Indonesia. Sistem kasir ini bertujuan untuk memberikan kemudahan kepada para pelanggan dalam melakukan transaksi belanja, termasuk transaksi jarak jauh. Berikut adalah definisi program tersebut:
## Nama Program: Sistem Kasir Self-Service Supermarket
## Deskripsi:
Program ini adalah implementasi sistem kasir self-service yang dibuat oleh Andi, pemilik supermarket besar di Indonesia. Sistem ini memungkinkan pelanggan untuk melakukan transaksi belanja dengan kemudahan dan fleksibilitas, termasuk dalam menambahkan, mengupdate, dan menghapus produk dalam daftar belanja mereka. Program ini juga mencakup fitur pembayaran dan perhitungan diskon berdasarkan total belanja.

## fitur-fitur dalam program kasir Anda:
1. Membuat ID dan Tanggal Transaksi Customer
2. Input Produk
3. Update Data Produk
4. Reset Transaksi
5. Pengecekan Daftar Belanja
6. Pembayaran

# Flowchart
![Alt text](image link)

# Penjelasan Kode Program
- __init__(self): Fungsi ini adalah konstruktor yang digunakan untuk inisialisasi objek transaksi. Ketika objek transaksi baru dibuat, self.cart (keranjang belanja) akan diinisialisasi sebagai daftar kosong.
- add_item(self, name, quantity, price): Fungsi ini digunakan untuk menambahkan item ke dalam keranjang belanja. Parameter name adalah nama produk, quantity adalah jumlah produk yang ingin dibeli, dan price adalah harga per produk. Item ini ditambahkan ke dalam daftar belanja.
- update_item_name(self, name, new_name): Fungsi ini memungkinkan pengguna untuk mengupdate nama produk dalam keranjang belanja. Dengan parameter name yang merupakan nama produk yang akan diubah dan new_name yang merupakan nama baru untuk produk tersebut.
- update_item_quantity(self, name, new_quantity): Fungsi ini memungkinkan pengguna untuk mengupdate jumlah produk dalam keranjang belanja. Dengan parameter name yang merupakan nama produk yang akan diubah dan new_quantity yang merupakan jumlah baru untuk produk tersebut.
- update_item_price(self, name, new_price): Fungsi ini memungkinkan pengguna untuk mengupdate harga produk dalam keranjang belanja. Dengan parameter name yang merupakan nama produk yang akan diubah dan new_price yang merupakan harga baru untuk produk tersebut.
- delete_item(self, name): Fungsi ini memungkinkan pengguna untuk menghapus produk dari keranjang belanja berdasarkan nama produk (name). Produk yang sesuai dengan nama yang diberikan akan dihapus dari keranjang belanja.
- reset_transaction(self): Fungsi ini mengosongkan seluruh daftar belanja (cart). Ketika digunakan, semua produk yang ada dalam keranjang belanja akan dihapus.
- total_price(self): Fungsi ini menghitung total harga dari semua item dalam keranjang belanja. Ini dilakukan dengan mengalikan jumlah item dengan harga per item dan menjumlahkannya.
- calculate_total_price(self): Fungsi ini juga menghitung total harga dari semua item dalam keranjang belanja, mirip dengan total_price(self). Ini digunakan dalam perhitungan diskon.
- apply_discount(self): Fungsi ini menghitung total harga belanjaan setelah menerapkan diskon. Jika total belanja lebih dari 500.000, akan diberikan diskon sebesar 10%. Jika total belanja lebih dari 300.000, akan diberikan diskon sebesar 8%. Jika total belanja lebih dari 200.000, akan diberikan diskon sebesar 5%. Jika tidak ada diskon yang diterapkan, total harga tetap sama.
- get_cart(self): Fungsi ini digunakan untuk mengakses daftar belanja (cart) dari objek transaksi. Ini memungkinkan pengguna atau program lain untuk melihat isi keranjang belanja.

# Penjelasan Alur Program
1. Customer masuk ke sistem dan memasukkan nama untuk mendapatkan ID transaksi.
    - Program akan meminta Customer untuk memasukkan ID transaksi dan tanggal transaksi.
    - Program akan menampilkan keranjang belanja kosong untuk memulai.
2. Customer memilih menu "1. Tambah Produk" untuk memasukkan nama-nama produk beserta jumlah dan harganya ke dalam daftar belanja.
    - Program akan meminta Customer untuk memasukkan nama produk, jumlah produk, dan harga per produk.
    - Data produk akan ditambahkan ke dalam keranjang belanja.
3. Apabila Customer salah memasukkan data, Customer dapat:
    - Memilih menu "2. Perbarui produk" untuk mengganti nama produk.
    - Memilih menu "3. Perbarui jumlah produk" untuk mengganti jumlah produk.
    - Memilih menu "4. Perbarui harga produk" untuk mengganti harga produk.
4. Apabila Customer merasa kurang yakin dengan produk-produk yang dibelanjakan, maka Customer dapat memilih "5. Hapus produk dari daftar".
    - Program akan meminta Customer untuk memasukkan nama produk yang ingin dihapus dari daftar belanja.
    - Produk tersebut akan dihapus dari keranjang belanja.
5. Jika Customer ingin mengosongkan daftar belanja dan memasukkan produk kembali, maka Customer dapat memilih "7. Reset daftar belanja".
    - Seluruh produk dalam keranjang belanja akan dihapus.
6. Customer dapat melihat daftar belanja dengan memilih menu "6. Cek daftar belanja".
    - Program akan menampilkan daftar produk yang ada dalam keranjang belanja beserta total harga.
7. Untuk melakukan pembayaran, Customer dapat memilih menu "8. Pembayaran".
    - Program akan menampilkan total harga dari produk dalam keranjang belanja.
    - Customer diminta untuk memasukkan jumlah uang pembayaran (dalam rupiah).
    - Program akan menghitung kembalian jika uang pembayaran mencukupi dan menampilkan pesan pembayaran berhasil.
# Test Case
## Test Case 1
Customer ingin menambahkan 2 item baru. Item yang ditambahkan adalah sebagai berikut:
- Nama item: Ayam goreng, Qty: 2, Harga: 20000
- Nama item: Pasta gigi, Qty: 3, Harga: 15000
  ![Alt text](image link)
# Test Case 2
Ternyata Customer salah membeli salah satu item dari belanjaan yang sudah ditambahkan, maka Customer dapat untuk menghapus item yang dipilih. Item yang ingin dihapus adalah Pasta gigi.
    ![Alt text](image link)
# Test Case 3
Ternyata setelah dipikir-pikir, Customer salah memasukkan item yang ingin dibelanjakan. Daripada menghapusnya satu-satu, maka Customer cukup menggunakan melakukan Reset Transaksi untuk menghapus semua item yang sudah ditambahkan. Daftar belanja setelah diperbarui:
    ![Alt text](image link)
# Test Case 4
setelah Customer selesai berbelanja, maka sistem akan menghitung total belanja yang harus dibayarkan. Sebelum mengeluarkan output total akan menampilkan daftar belanja. Daftar belanja ketika melakukan pembayaran:
    ![Alt text](image link)
