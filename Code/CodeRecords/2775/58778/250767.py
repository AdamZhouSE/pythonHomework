n=int(input())
for i in range(n):
    m=int(input())
    if((m-3)%3!=0):
        print(-1)
    else:
        x=int((m-3)/3)
        print(x,'',end='')
        print(x+1,'',end='')
        print(x+2)