#menu kafe anu
menus = {
    "Americano":10000,
    "Kopi Susu":8000,
    "Black Tea":15000,
}
print("--------------Kafe Anu Menu's---------------")
print("........Ngopi Asyik, Tanpa Berisik..........")
for i in menus :
    print("Daftar Menu: ", i,"\t Harga: ",menus[i])
print("--------------------------------------------")
nama = input ("Nama Pelanggan: ")
pesanan = input ("Pilih Menu: ") 
jumlah = int(input("Jumlah Pesanan: "))
bayar = jumlah * menus[pesanan]

print("-------------Detil Pembayaran---------------")
print("Nama Pelanggan : ",nama)
print("Menu yang dipesan : ",pesanan)
print("Jumlah yang dipesan :",jumlah)
print("Total Bayar: ",bayar)
