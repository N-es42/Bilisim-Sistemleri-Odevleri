# ENES KUCUKATALAY 19410051045 YBS 3.SINIF NO
# Şifreleme ve Çözme 
# 1- Şifrelemek için kullanıcı bir kelime ve key verir. Karşılığında key kadar ilerletilmiş karışık text i verir.
# 2- Şifre çözmek için kullanıcı karışık text i verir ve doğru key i vermesi durumunda şifreyi çözer.
def main():
    print(" Hoşgeldiniz...")
    print("Bir seçim yapınız: ")
    print("Şifrelemek için 1 ")
    print("Şifrelenmiş veriyi çözmek için 2")
    secim = input("Seçiminiz: ")
    if (secim=="1"):
        sifrele()
    elif (secim=="2"):
        sifreliCoz()
    else:
        print("Yanlış seçim yaptınız...")

 # ana text e eklemek için onun uzunluğunda key dizisi üretir.
 # Orneğin kelime= enes ve key= x olsun Üretilen dizi=[x,x,x,x]
def keydizi(alinan_metin):
    keyGir = input("bir key giriniz: ")

    sifrekelime=alinan_metin

    listKey= list(keyGir)
    listKelime= list(sifrekelime)

    anahtarascii=[]

    for i in range(len(listKelime)): 
        for j in listKey:
            if(len(anahtarascii)<len(listKelime)):
                anahtarascii.append(ord(j))


    return anahtarascii

def sifrele():
    alinan_metin = input("Şifrelenecek veriyi gir: ")
    anahtarascii=keydizi(alinan_metin) # girilen kadar dizi fonksiyonunu çalıştırdık.
    Kontrol1= alinan_metin.strip()
    Kontrol1=kontrol(Kontrol1)
    alinan_metin=Kontrol1
    alinan_metin_ascii=[]

    # alınan metni ascii koduna dönüştürdük
    for karakter in alinan_metin:
        alinan_metin_ascii.append(ord(karakter))

    # anahtar ile alınanı topladık
    toplam_dizisi=[]
    for i in range(len(alinan_metin_ascii)):
        x=0
        x=anahtarascii[i]+alinan_metin_ascii[i] 
        mod=0
        mod= x % 126
        mod=mod+33
        toplam_dizisi.append(mod)

    # sifreleme
    sifreleList=[]
    for j in toplam_dizisi:
        sifreleList.append(chr(j))
    sifreli_metin=listToString(sifreleList)
    print("Şifrelenmiş veri:  ")
    print(sifreli_metin)

################

def sifreliCoz():
    girilenText = input("Çözülecek Şifreli veriyi gir: ")
    anahtarascii=keydizi(girilenText) # girilen kadar dizi 
    girilenTextList=[]
    for harf in girilenText:  # alınan metni ascii koduna dönüştürdük
        girilenTextList.append(ord(harf))
    ilk=0
    ekstra=0
    toplam=0
    sifre=0
    liste=[]
    for y in range(len(girilenTextList)): # şifreleme işleminin ters işlemini yapıyoruz.
        sifre = girilenTextList[y]        # bu şekilde doğru kelimeye ulaşıyoruz.
        ilk=sifre-33
        ekstra = 126-anahtarascii[y]
        toplam=ilk+ekstra
        liste.append(toplam)

    sifreCozList=[]
    for u in liste:
        sifreCozList.append(chr(u))

    sonuc=listToString(sifreCozList)
    sonuc=sonuc.replace("_"," ")    

    print("Şifrenin Çözülmüş Hali: " , sonuc)

# yardımcı fonksiyonlar
def listToString(s): 
    metin = "" 
    for harf in s: 
        metin += harf  
    return metin 
def kontrol(kelime):
    Kontrol1= kelime
    Kontrol1= Kontrol1.replace(" ","_")
    Kontrol1= Kontrol1.replace("ğ","g")
    Kontrol1= Kontrol1.replace("Ğ","G")
    Kontrol1= Kontrol1.replace("ı","i")
    Kontrol1= Kontrol1.replace("İ","I")
    Kontrol1= Kontrol1.replace("ö","o")
    Kontrol1= Kontrol1.replace("Ö","O")
    Kontrol1= Kontrol1.replace("ü","u")
    Kontrol1= Kontrol1.replace("Ü","U")
    Kontrol1= Kontrol1.replace("ş","s")
    Kontrol1= Kontrol1.replace("Ş","S")
    Kontrol1= Kontrol1.replace("ç","c")
    Kontrol1= Kontrol1.replace("Ç","C")
    return Kontrol1


main()
