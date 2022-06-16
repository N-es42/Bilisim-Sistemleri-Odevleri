# 19410051045 Enes Kucukatalay YBS 3.SINIF NO
# Offset olarak bir sayı girip türkçe düzgün kelime alır. Size test için ilerletilmis karısık text i verir.
# Bu kodlar size yardımcı olması için yapılmıştır. Ana dosya main_offset_bul dosyasıdır.
# buradan cıkan ornegi main_offset_bul da deneyebilirsiniz.

offset = int(input("ofset gir: "))
kelime = input("Turkce bir kelime gir: ")
kelime=kelime.lower()
turkce_harf=["a","b","c","ç","d","e","f","g","ğ","h","ı","i","j","k","l","m","n","o","ö","p","r","s","ş","t",
            "u","ü","v","y","z"]

sifreli=[]
indexler=[]
for i in kelime:
    indexler.append(turkce_harf.index(i))

indexArtı=[]
for i in range(len(indexler)):
    x=0
    x = indexler[i]+offset
    x = x % 29
    indexArtı.append(x)

dizi=[]
for i in indexArtı:
    dizi.append(turkce_harf[i])
print(dizi)
sifrelikelime=""
for i in dizi:
    sifrelikelime+=i
print(sifrelikelime)
