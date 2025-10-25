#basit hesap makinesi - 2 sayıdan oluşan işlemler
sayi1 = float(input("Birinci sayıyı giriniz: "))
sayi2 = float(input("İkinci sayıyı giriniz: "))
print("Yapacağınız işlemi seçiniz: ")
print("1- Toplama\n2- Çıkarma\n3- Çarpma\n4- Bölme")
işlem = input("İşlem numarasını giriniz (1/2/3/4): ")
if işlem == '1':
    print(sayi1, "+", sayi2, "=", sayi1 + sayi2)
elif işlem == '2':
    print(sayi1, "-", sayi2, "=", sayi1 - sayi2)
elif işlem == '3':
    print(sayi1, "*", sayi2, "=", sayi1 * sayi2)
elif işlem == '4':
    if sayi2 == 0:
        print("Hata: Hiçbir sayı sıfıra bölünemez.")
    else:
        print(sayi1, "/", sayi2, "=", sayi1 / sayi2)