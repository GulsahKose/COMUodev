n = int(raw_input("Kacinci fibonanchi sayisini girmek istediginizi giriniz: "))

def fibonanchi(n):
   if n <= 1:
       return n
   else:
       return(fibonanchi(n-1) + fibonanchi(n-2))

print fibonanchi(n)
