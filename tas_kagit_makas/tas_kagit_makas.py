import random
secenek = ["tas","kagit","makas"]
tas=secenek[0]
kagit=secenek[1]
makas=secenek[2]

print("Oyuna hoşgeldiniz çıkmak için q tuşuna basın ")

while True:
    secim=input("Tas mı Kagit mı Makas mı: ")
    pc_secim= random.choice(secenek)
    
    if secim==tas:
        if pc_secim==tas:
            print("Bilgisayarın secimi tas. Berabere")

        elif pc_secim==kagıt:
            print("Bilgisayarın secimi kagıt. Kaybettiniz")

        elif pc_secim==makas:
            print("Bilgisayarın secimi makas. Kazandınız")

    if secim==kagit:
        if pc_secim==tas:
            print("Bilgisayarın secimi tas. Kazandınız")

        elif pc_secim==kagıt:
            print("Bilgisayarın secimi kagıt. Berabere")

        elif pc_secim==makas:
            print("Bilgisayarın secimi makas. Kaybettiniz")

    if secim == makas:
        if pc_secim==tas:
            print("Bilgisayarın secimi tas. Kaybettiniz")

        elif pc_secim==kagıt:
            print("Bilgisayarın secimi kagıt. Kazandınız")

        elif pc_secim==makas:
            print("Bilgisayarın secimi makas. Berabere")

    if secim==quit:
        print("çikiiyor...")
        break



