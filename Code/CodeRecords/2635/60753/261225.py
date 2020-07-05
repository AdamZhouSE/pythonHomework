import math
def factorial(x):
    i=x
    res=1
    while i!=1:
        res=res*i
        i-=1
    return res
k=input()
if k==0:
    print(5)
else:
    count=0
    i=5
    ceiling=math.pow(10,9)
    while factorial(i)<=ceiling:
        if (factorial(i)%(int(math.pow(10,k))))==0 and (factorial(i)%(int(math.pow(10,k+1))))==0:
            count+=1
        i+=1
    print(count)
                                                       
                                                                  
    