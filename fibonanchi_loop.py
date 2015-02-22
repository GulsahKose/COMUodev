import time

start = time.time()

def fibonanchi(n):
    if n == 1 or n == 2:
	return 1;
    else: 
        fib1=1
        fib2=1
        i=2
        while (n>=i):
	    fibonacci = fib1 + fib2;
	    fib1 = fib2;
            fib2 = fibonacci;
            i=i+1
        return fibonacci; 

print fibonanchi(5)

end = time.time()

print "%2f" %(end-start)
