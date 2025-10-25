yas = input("Lütfen yaşınızı giriniz: ")
try :
    yas = int(yas)
    if yas < 0:
        print("Hata: Yaş negatif olamaz.")
    else:
        print("Yaşınız:", yas)
except ValueError:
    print("Hata: Lütfen geçerli bir sayı giriniz.")
# Hata yakalama örneği - Kullanıcıdan yaş bilgisi alma