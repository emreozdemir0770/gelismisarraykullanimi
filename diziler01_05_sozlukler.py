# -*- coding: utf-8 -*-

#oluşturma
notlar={"emre":75,"rana":96,"barış":85,"ırmak":88,"tuğçe":96}

#ekleme
notlar["leyla"]=89

#yazdırma
print(notlar)


#sadece istenileni yazdırma
print(notlar["emre"])

#tüm listeyi temizle
notlar.clear()


#sadece eçileni sil
notlar.pop("rana")

#rastgele birisini çıkarıyor
notlar.popitem()



notlar2=notlar.copy()
print(notlar2)



