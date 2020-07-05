import math
p=int(input())
q=int(input())
i=0
while(true):
    if(i%2==0):
        if((i*q)%(2*p)==p):
            print(2)
            break
    else:
        if((i*q)%(2*p)==p):
            print(1)
            break
		else if((i*q)%(2*p)==0):
            print(0)
            break
    i=i+1
