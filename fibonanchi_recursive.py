import time

start = time.time()

def fibonanchi(n):
   if n <= 1:
       return n
   else:
       return(fibonanchi(n-1) + fibonanchi(n-2))

print fibonanchi(10)

end = time.time()

print "%2f"%(end-start)
