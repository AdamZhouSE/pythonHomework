k=int(input())
m=k%10
if(m==2 or m==4 or m==5 or m==6 or m==8 ):
    print(-1)
else:
    if(1%k==0):
        print(1)
    elif(11%k==0):
        print(2)
    elif(111%k==0):
        print(3)
    elif(1111%k==0):
        print(4)
    elif(11111%k==0):
        print(5)
    
    else:
        print(-1)