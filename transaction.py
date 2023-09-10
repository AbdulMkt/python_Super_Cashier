class Transaction:
    def __init__(self):
        self.cart = []  # Menambahkan atribut cart sebagai daftar item dalam transaksi

    def add_item(self, name, quantity, price):
        item = {"name": name, "quantity": quantity, "price": price}
        self.cart.append(item)

    def update_item_name(self, name, new_name):
        for item in self.cart:
            if item["name"] == name:
                item["name"] = new_name  # Memperbarui nama item dalam keranjang belanja

    def update_item_quantity(self, name, new_quantity):
        for item in self.cart:
            if item["name"] == name:
                item["quantity"] = new_quantity  # Memperbarui jumlah item dalam keranjang belanja

    def update_item_price(self, name, new_price):
        for item in self.cart:
            if item["name"] == name:
                item["price"] = new_price  # Memperbarui harga item dalam keranjang belanja

    def delete_item(self, name):
        self.cart = [item for item in self.cart if item["name"] != name]  # Menghapus item dari keranjang belanja

    def reset_transaction(self):
        self.cart = []  # Mengosongkan daftar belanja

    def total_price(self):
        total = sum(item["quantity"] * item["price"] for item in self.cart)
        return total  # Menghitung total harga semua item dalam keranjang belanja

    def calculate_total_price(self):
        return sum(item["quantity"] * item["price"] for item in self.cart)  # Menghitung total harga semua item dalam keranjang belanja

    def apply_discount(self):
        total = self.calculate_total_price()
        if total > 500000:
            return total * 0.9  # Diskon 10% jika total lebih dari 500.000
        elif total > 300000:
            return total * 0.92  # Diskon 8% jika total lebih dari 300.000
        elif total > 200000:
            return total * 0.95  # Diskon 5% jika total lebih dari 200.000
        return total  # Mengembalikan total harga setelah diskon (jika ada)

    def get_cart(self):
        return self.cart  # Menambahkan metode get_cart untuk mengakses daftar belanja (cart)
