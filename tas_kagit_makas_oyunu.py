import random
print(30*"*"+"Taş Kağıt Makas Oyunu"+30*"*")
liste=["Taş","Kağıt","Makas"]


while True:
  
  while True:
     secim=int(input("Taş kağıt makas oyununa hoşgeldiniz.Oyunda taş demek için 0,kağıt için 1 makas için 2 yi tuşlayınız:"))
     if 0<=secim<=2:
        break
     else:
        print("Geçersiz bir karakter girdiniz...")
  kullanıcısecim=liste[secim]
  pcsecim=random.choice(liste)
  print(f"Sizin seçiminiz:{kullanıcısecim}\nBilgisayarın seçimi:{pcsecim}")

  if kullanıcısecim==pcsecim:
     print("Berabere")
  elif (kullanıcısecim == "Taş" and pcsecim == "Makas")  or (kullanıcısecim == "Kağıt" and pcsecim == "Taş") or (kullanıcısecim == "Makas" and pcsecim == "Kağıt"):
        print("Tebrikler kazandınız")
  else:
        print("Kaybettiniz")
  
  cıkıssecim=int(input("Tekrar oynamak istiyorsanız 1e çıkmak istiyorsanız 2ye basınız:"))
  if cıkıssecim == 2:
     print("Oyundan çıkılıyor...")
     break 
     
 
