
cıkıs=1
while cıkıs==1:
    soru = input("toplama=1 çıkarma=2 çarpma=3 bölme=4 (çıkmak için q)")

if soru == "q":
        print("çıkılıyor...")
        cıkıs=0

elif soru=="1":
    s1=input("1.sayıyı girin: ")
    s2=input("2.sayıyı girin: ")
    toplam=float(s1)+float(s2)
    print("sonuc" + toplam)

elif soru == "2":
    s3=input("1.sayıyı girin: ")
    s4=input("2.sayıyı girin: ")
    fark=float(s1)-float(s2)
    print("sonuc" + fark)
   
elif soru == "3":
    s5=input("1.sayıyı girin: ")
    s6=input("2.sayıyı girin: ")
    carpım=float(s1)*float(s2)
    print("sonuc" + carpım)

elif soru == "4":
    s7=input("1.sayıyı girin: ")
    s8=input("2.sayıyı girin: ")
    bolum=float(s1)/float(s2)
    print("sonuc" + bolum)

else:
    print("yanlış giriş")


