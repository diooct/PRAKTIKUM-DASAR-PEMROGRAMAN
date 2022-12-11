menu = "y" or "Y"
while menu == "y" or "Y":
    print(" ========================================")
    print(" kirim.com")
    print(" jl harapan baru")

    print(" ========================================")
    print(" Tipe layanan pengiriman")
    print(" ========================================")
    print(" 1. Same day : Rp 30.000")
    print(" 2. Super (kilat) : Rp 20.000")
    print(" 3. Eksekutif : Rp 18.500")
    print(" 4. Reguler : Rp 12.000")
    print(" 5. Ekonomi : Rp. 10.000")
    print(" ========================================")
    tipelayananpengiriman=str(input(" Masukkan angka sesuai dengan layanan yang tersedia : "))
    beratpaketkg=int(input(" berat paket : "))
    nama = input("nama pengirim :")
    notelp = input("no telp :")
    nama2 = input("nama penerima :") 
    kotatujuan = input("kota tujuan :")
    isipaket = input("Isi paket :")
    if tipelayananpengiriman == "1":
        tipelayanan= " Same day"
        harga=(30000*beratpaketkg)
        pajak= (2500)
        totalharga=int(harga+pajak)
    elif tipelayananpengiriman == "2":
        tipelayanan= " Super (kilat)"
        harga=(20000*beratpaketkg)
        pajak= (2500)
        totalharga=int(harga+pajak)
    elif tipelayananpengiriman == "3":
        tipelayanan= " Eksekutif "
        harga=(18500*beratpaketkg)
        pajak= (2500)
        totalharga=int(harga+pajak)
    elif tipelayananpengiriman == "4":
        tipelayanan= " Reguler "
        harga=(12000*beratpaketkg)
        pajak= (2500)
        totalharga=int(harga+pajak)
    elif tipelayananpengiriman == "5":
        tipelayanan= " Ekonomi "
        harga=(10000*beratpaketkg)
        pajak= (2500)
        totalharga=int(harga+pajak)
    else:
        layanan=input(" Mohon maaf,layanan yang anda pilih tidak tersedia, terima kasih")

    print(" ------------------------------")
    print(" Nama pengirim :", nama)
    print(" No telp :", notelp)
    print(" Nama penerima :", nama2)
    print(" Kota tujuan :", kotatujuan)
    print(" Isi paket :", isipaket)
    print(" Tipe layanan :",tipelayananpengiriman)
    print(" Berat paket :", beratpaketkg)
    print(" Harga :", harga)
    print(" Pajak :", pajak)
    print(" ------------------------------")
    print(" Total :", totalharga)
    print(" ------------------------------")
    print(" terima kasih sudah memakai jasa kami ")

    import time

    tanggal = time.strftime("%d-%m-%y-%H:%M:%S")
    print(tanggal)
    print(type(tanggal))

    print("           www.kirim.com         ")
    print("=================================")
    layanan=input(" apa anda ingin menambah pengiriman lagi? pilih Y jika Ya, pilih N jika Tidak (Y/N) = ")