
import math
def isPrime(i):
	re = True
	if(i==2):
		return True
	if(i%2==0):
		return False
	x=3
	while(x<=int(math.sqrt(i))):
		if(i%x==0):
			re = False
			break
		x+=2
	return re
n = int(input())
prime = 0
if(n==1 and n==2):
    prime = 0
else:
    arrange = 0
    for i in range(2,n+1):
        if(isPrime(i)):
            prime+=1
    composite = n-prime
    re = 0
    num_prime = 1
    num_com = 1
    for i in range(1,prime+1):
        num_prime *= i
    for i in range(1,composite+1):
		
        num_com *= i
    print((num_prime*num_com)%1000000007)
