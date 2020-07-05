N=int(input())
for i in range(N):
    s=int(input())
    if s==2:
        print(2)
    if s==3:
        print(4)
    elif s==4:
        print(6)
    else:
        print((s-1)*2)