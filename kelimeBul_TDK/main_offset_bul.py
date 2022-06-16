# ENES KUCUKATALAY 19410051045 YBS 3.SINIF NO
# Karışık olan ilerletilmiş olan text i alıp 29 kadar ilerletip, TDK kelimeleri ile karşılaştırır.
# Eğer karışık kelimeniz yoksa artir.py dosyamdan faydalanabilirsiniz.
turkce_harf=["a","b","c","ç","d","e","f","g","ğ","h","ı","i","j","k","l","m","n","o","ö","p","r","s","ş","t",
            "u","ü","v","y","z"]

text = input('Şifreli text gir:')
text1=text
# key = ? 
text =list(text)   # Alınan kelimeyi harfe çevir.

kelimeler=[]

for i in range(1,30):  # offseti 1 den 29 a kadar artırarak kelimelerin yeni halini diziye attık.
    word=""            # Burada bir dizi çıkıyor içindeki bir kelime doğru kelime.
    for j in text:
        harfIndis= turkce_harf.index(j)
        harfIndis += i    
        harf=turkce_harf[harfIndis%29]
        word += harf
    kelimeler.append(word)

# print(kelimeler)
dosya = open("tdk.txt","r",encoding="UTF-8") # Tdk kelimelerinin dosyasını actım.

liste= dosya.readlines()            # Tüm kelimeleri bir diziye attım.

kelimeler_dizisi=[]
for i in range(len(liste)-1):       # Her satırda bosluk olduğu için boslukları temizledim.
    kelime=""
    kelime=liste[i].strip()
    kelimeler_dizisi.append(kelime)

print("****")
print("")
print("Şifreli text", text1)
# Burada en başta yaptığımız 1-29 ilerletilmiş diziyi Tdk kelimelerinin bulunduğu dizi ile karşılaştırıyorum.
for i in range(len(kelimeler)-1):        
    for j in range(len(kelimeler_dizisi)-1): 
        if (kelimeler[i]==kelimeler_dizisi[j]): # her kelime denenir eşit çıkan kelime doğrudur.
            print(kelimeler_dizisi[j], " -> TDK da bulunan kelime.")
            offset=kelimeler.index(kelimeler[i])+1
            print( "Şifreyi kırman için ilerletmen gereken offset=", offset )
            

print("Şifreleme metodunun uyguladığı offset -> ", 29-offset)
