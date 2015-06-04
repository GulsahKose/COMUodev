dizi = "00110000000000000001110000"

def bul(dizi):
  uzunluk = len(dizi)
  maxboyut=0
  boyut=0
  for i in range(0,uzunluk):
    if dizi[i] == '0':
      boyut=boyut+1
      if i == uzunluk-1:
        if boyut > maxboyut:
          maxboyut = boyut
          boyut=0
    else:
      if boyut > maxboyut:
        maxboyut = boyut
        boyut=0
  return maxboyut

print bul(dizi)

