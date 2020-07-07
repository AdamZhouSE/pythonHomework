import math
def check(n):
    for i in range(2,int(math.sqrt(n))+1):
        if (n%i ==0):
           return 0 
           break
    else:
        return 1
        
t= int(input())
while(t):
    a,b = map(int,input().split())
    k=0
    p = a+b+1
    while(k==0):
        if (check(p)==0):
            p+=1
        else:
            print(p-a-b)
            k =1
            
    t =t-1