N=int(input())
for i in range(N):
    num=int(input())
    j=0
    while True:
        if j*j*j==num:
            print(j)
            break
        elif j*j*j>num:
            print(j-1)
            break
        else:
            j+=1