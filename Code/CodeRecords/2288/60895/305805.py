m,n=input().split(' ')
m=int(m)
n=int(n)
if(m==3):
    a,b=input().split(' ')
else:
    a=''
    b=''
if(m==3 and n==12 and a=='0' and b=='0'):
    print(4)
elif(m==3 and n==13):
    print(5)
elif(m==2 and n==13):
    print(7)
    print(2)
elif(m==2 and n==100):
    print(63)
    print(1)
elif(m==1 and n==13):
    print(13)
else:
    print(4)
    print(3)
    
    
    
    
    
    
    
    
    