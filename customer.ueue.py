class Transaksi:
    def _init_(self, customer_name, transaksi_type):
        self.customer_name = customer_name
        self.transaksi_type = transaksi_type

class transaksiQueue:
    def _init_(self):
        self.queue = []

    def add_transaksi(self, transaksi):
        self.queue.append(transaksi)
        print(f"Transaksi '{transaksi.transaksi_type}' oleh {transaksi.customer_name} telah ditambahkan ke dalam antrian.")

    def serve_transaksi(self):
        if len(self.queue) > 0:
            transaksi = self.queue.pop(0)
            print(f"Transaksi '{transaksi.transaksi_type}' oleh {transaksi.customer_name} telah dilayani.")
        else:
            print("Antrian transaksi kosong.")

    def next_transaksi(self):
        if len(self.queue) > 0:
            transaksi = self.queue[0]
            print(f"Transaksi berikutnya: '{transaksi.transaksi_type}' oleh {transaksi.customer_name}.")
        else:
            print("Antrian transaksi kosong.")

    def display_transaksis(self):
        if len(self.queue) > 0:
            print("Transaksi yang tersimpan:")
            for transaksi in self.queue:
                print(f"'{transaksi.transaksi_type}' oleh {transaksi.customer_name}")
        else:
            print("Antrian transaksi kosong.")


transaksi_queue = transaksiQueue()

while True:
    print("\nMenu:")
    print("1. Tambahkan transaksi")
    print("2. Layani transaksi berikutnya")
    print("3. Tampilkan transaksi berikutnya")
    print("4. Tampilkan semua transaksi")
    print("5. Hapus transaksi yang telah dilayani")
    print("6. Keluar")

    choice = input("Pilih tindakan (1/2/3/4/5/6): ")

    if choice == "1":
        customer_name = input("Masukkan nama pelanggan: ")
        transaksi_type = input("Masukkan jenis transaksi: ")
        transaksi = Transaksi(customer_name, transaksi_type)
        transaksi_queue.add_transaksi(transaksi)
    elif choice == "2":
        transaksi_queue.serve_transaksi()
    elif choice == "3":
        transaksi_queue.next_transaksi()
    elif choice == "4":
        transaksi_queue.display_transaksis()
    elif choice == "5":
        transaksi_queue.serve_transaksi()
    elif choice == "6":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid.")