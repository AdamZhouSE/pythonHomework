#a乘2 -1==b除以2 +1
#if b偶：b/2  
#if b奇：b+1 直到b=a

a=int(input())
b=int(input())
count=0
while(b!=a):
    if b%2==0:
        b=b/2
    else:
        b=b+1
    count=count+1   
print(count)    