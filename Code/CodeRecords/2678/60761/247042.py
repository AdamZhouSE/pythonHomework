n=int(input())
for i in range(n):
    k=1
    a=int(input())
    while(True):
        if(a==1):
            print(k)
            break
        else:
            if(a%2==1):
                print("-1")
                break
            else:
                k=k+1
                a=int(a/2)