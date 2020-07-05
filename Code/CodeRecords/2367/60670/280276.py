k=int(input())
if k%2==0:
    print(-1)
else:
    t=0
    leng=0
    while True:
        t=t*10+1
        leng+=1
        if t%k==0:
            print(leng)
            break