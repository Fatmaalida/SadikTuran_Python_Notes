diller = ["Python","C#","Java","Javascript","React"]

sonuc = diller
sonuc = type(diller)
sonuc = diller[0:2]
sonuc = diller[2:]  #2.den başla sonuna kadar al  -->java javascript react
sonuc = diller[:3]  #3. dahil olmadan al --> python c# java
sonuc = diller[-1]
sonuc = diller[-4:-1] #-4 den başla -1 e kadar --> c# java javascript sondaki dahil değil
# diller[0] = "Html"  -->python htmle dönüşür
diller[-1] = "Html"
sonuc = len(diller)
sonuc = diller + ["Angular","Vuejs"]

# if bloğu=> Koşul ifadeleri
if "Python" in diller:
    print("değer listenin bir elemanı")

# döngüler
for x in diller:
    print(x)

del diller[0]

sonuc = diller

print(sonuc)