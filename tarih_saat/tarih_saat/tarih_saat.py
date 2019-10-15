import time

while True:

    tarih= time.localtime()
    yil = tarih[0]
    ay = tarih[1]
    gun = tarih[2]

    zaman= time.localtime()
    saat = zaman[3]
    dakika = zaman[4]
    saniye = zaman[5]

    time.sleep(2)


    print ("tarih: {}/{}/{}  ".format(gun,ay,yil))
    print ("saat: {}.{}.{}".format(saat,dakika,saniye))
