
#Tugas : Buatlah Coding yang menghasilkan hasil "Budi membeli satu botol susu dan enam butir telur jika di toko ada telur"

#Sekuensial
print('Ibu berkata,"Pergi ke toko"')
print('Budi Menjawab, "Baik, apa yang harus saya lakukan di toko?"')
print('Ibu berkata," Jika di toko ada telur, Belikan satu botol susu dan enam butir telur"')
print('Maka Budi berangkat ke toko')

#Percabangan
jumlah_botol_susu = 173
jumlah_telur = 1587

print(f"jumlah botol susu {jumlah_botol_susu} botol")
print(f"jumlah telur {jumlah_telur} butir")

if jumlah_botol_susu > 0:
    print("Budi Mengecek harganya, dan uangnya ternyata cukup")

    if jumlah_telur > 0:
        print("Budi membeli 1 botol susu")
        print("Budi membeli 6 butir telur")

    else:
         print("Budi membeli 6 botol susu")

else:
    print("Budi tidak membeli botol susu")


print("Budi pulang ke rumah")
print("Budi menyampaikan hasilnya kepada ibunya")