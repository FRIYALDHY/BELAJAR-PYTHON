def hitung_profit():

    print("===KALKULATOR BISNIS===")

nama_produk = input("Nama Produk")
harga_jual = int(input("Harga Jual per Unit : "))
modal = int(input("Modal per Unit : "))
jumlah_terjual = int(input("Jumlah Terjual : "))

omzet = harga_jual * jumlah_terjual
total_modal = modal * jumlah_terjual
profit = omzet - total_modal

print("\n=====HASIL=====")
print("Produk       :", nama_produk)
print("Omzet        :", omzet)
print("Total Modal  :", total_modal)
print("Profit       :", profit)

hitung_profit ()