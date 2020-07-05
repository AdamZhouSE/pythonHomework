t=int(input())
for i in range(0,t):
    n=int(input())
    counter=1
    while(True):
        if counter**3<=n:
            counter+=1
        else:
            counter-=1
            break
    print(counter)