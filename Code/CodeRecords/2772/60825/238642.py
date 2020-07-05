N=int(input())
for i in range(N):
    num=int(input())
    j=0
    while True:
        if j*j*j==num:
            print(j)
            break
        elif j*j*j>num:
            print(j)
            break
        else:
            j+=1