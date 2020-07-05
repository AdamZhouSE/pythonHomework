N=int(input())
for i in range(N):
    num=int(input())
    j=0
    while true:
        if j*j==num:
            print(1)
            break
        else if j*j<num:
            j+=1
        else:
            print(0)
            break