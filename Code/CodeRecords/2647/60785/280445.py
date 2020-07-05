t=int(input())
for test in range(t):
    n=int(input())
    res=0
    if n==1:
        print(1)
    elif(n==5):
        print(2)
    elif( n!=1 and n!=5):
        print(3)
        res+=1
    if(res!=0):
        print(4)
    
   