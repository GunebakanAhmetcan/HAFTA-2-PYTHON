#Kullanıcı tarafından girilen iki sayıyı toplayan fonksiyon
def toplama(a, b):
    """
    İki sayıyı toplayan fonksiyon.
    """
    return a+b 
help(toplama)
Sayi1 = int(input("Birinci sayıyı giriniz: "))
Sayi2 = int(input("İkinci sayıyı giriniz: "))
x = toplama(Sayi1, Sayi2)

print("Toplam:", x)

