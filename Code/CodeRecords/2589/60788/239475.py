from sys import stdin 

def lucas(n):
    if n==0:
        return 2
    elif n==1:
        return 1
    else:
        a=2
        b=1
        while n-2>=0:
            n-=1
            temp=b
            b=a+b
            a=temp
        return b
            
        
num=int(stdin.readline().strip())
for i in range(0,num):
    v=int(stdin.readline().strip())
    print(lucas(v)%1000000007)
    