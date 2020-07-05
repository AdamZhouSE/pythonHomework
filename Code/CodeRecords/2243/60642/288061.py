p = int(input())
q = int(input())
for i in range(1,1000):
    if((p*i/q)%1==0):
        if(i%2==0):
            print(0)
        elif((p*i/q)%2==1):
            print(1)
        else:
            print(2)
        break