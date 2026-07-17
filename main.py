def coffee_bot():
    print("CoffeeBot: Halo! Selamat datang di CoffeeBot. Ada yang bisa saya bantu hari ini?")
    print("1. Lihat Menu\n2. Tanya Jam Operasional\n3. Keluar")
    
    menu = {
        "1": {"nama": "Espresso", "harga": 20000},
        "2": {"nama": "Caffè Latte", "harga": 25000},
        "3": {"nama": "Cappuccino", "harga": 25000},
        "4": {"nama": "Americano", "harga": 22000}
    }

    while True:
        pilihan = input("\nAnda: ")
        
        if pilihan == "1" or "menu" in pilihan.lower():
            print("\nCoffeeBot: Berikut menu andalan kami hari ini:")
            for kunci, item in menu.items():
                print(f"{kunci}. {item['nama']} - Rp {item['harga']:,}")
            
            pesan = input("\nCoffeeBot: Pilih nomor menu yang ingin Anda pesan (atau ketik 'batal'): ")
            if pesan in menu:
                jumlah = int(input("CoffeeBot: Berapa jumlah yang ingin dipesan? "))
                total = menu[pesan]['harga'] * jumlah
                print(f"\nCoffeeBot: Pesanan Anda berhasil dicatat! {jumlah}x {menu[pesan]['nama']}.")
                print(f"Total yang harus dibayar: Rp {total:,}. Terima kasih!")
            else:
                print("CoffeeBot: Pemesanan dibatalkan atau pilihan tidak valid.")
                
        elif pilihan == "2" or "jam" in pilihan.lower():
            print("\nCoffeeBot: Kami buka setiap hari mulai pukul 08.00 pagi sampai 22.00 malam. Kami tunggu kedatangannya!")
            
        elif pilihan == "3" or "keluar" in pilihan.lower():
            print("\nCoffeeBot: Terima kasih telah menghubungi CoffeeBot. Sampai jumpa!")
            break
        else:
            print("\nCoffeeBot: Maaf, saya tidak mengerti. Silakan pilih menu 1, 2, atau 3.")

# Menjalankan chatbot
if __name__ == "__main__":
    coffee_bot()
