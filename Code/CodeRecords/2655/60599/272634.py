def mi(k):
    while(k>1):
        if(k%2!=0):
            return False
        k=k//2
    return True

u=int(input())
for z in range(u):
    n=int(input())
    while 1:
        if(mi(n)):
            print(n)
            break
        n+=1