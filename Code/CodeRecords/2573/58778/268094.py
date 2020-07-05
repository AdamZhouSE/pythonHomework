n=int(input())
for i in range(n):
    m=int(input())
    if(m%2==0):
        if(m!=2):
            k=int(m/2)-1
            print(int(pow(2,pow(3,k))))
        else:
            print(2)
    else:
        if(m!=1):
            k=int(m/2)
            print(int(pow(2,pow(2,k))))
        else:
            print(2)
