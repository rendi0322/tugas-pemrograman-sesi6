umur = int(input("Masukan umur anak (tahun): ")) 
tinggi = int(input("Masukan tinggi anak (CM): ")) 
harga = 0 
textHarga = "harga untuk anak dengan umur {} tahun dengan tinggi {} cm adalah {} rupiah" 

if (umur < 2 ):
    print("Dilarang masuk") 
elif (umur < 4): 
    harga = 30_000 
    if (tinggi > 70):
        harga += 10_000 
    print(textHarga.format(umur, tinggi, harga)) 
elif (umur < 7): 
    harga = 40_000 
    if (tinggi > 120): 
        harga += 15_000 
    print(textHarga.format(umur, tinggi, harga)) 
elif (umur < 10): 
    harga = 50_000 
    if (umur > 7 and tinggi > 150): 
        harga += 20_000 
    print(textHarga.format(umur, tinggi, harga)) 
else: 
    harga = 80_000 
    print(textHarga.format(umur, tinggi, harga))