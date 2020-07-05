a=int(input())
for k in range(0,a):
    a=input()
    b = input().split(' ')
    he=int(input())
    is0=1
    for i in range(0, len(b)):
        b[i] = int(b[i])
    for i in range(0,len(b)-1):
        for j in range(i+1,len(b)):
            if b[i]+b[j]==he:
                print(b[i],end=" ")
                print(b[j],end=" ")
                print(he)
                is0=0
    if is0==1:
        print(-1)