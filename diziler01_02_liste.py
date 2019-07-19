# -*- coding: utf-8 -*-

#dizileri oluşturma
a=["emre","mehmet","okan","barcın"]

#ekleme
a.append("büşra")

#çıkarma
a.remove("barcın")


#index sırasına göre çıkarma
del(a[2])


#☻tersten okunması için
a.reverse()

#alfabetik sıralama sokma
a.sort()


#arama yapma (varsa 1 yoksa 0) 
print(a.count("emre"))

#yazdırma 
print(a)
