n=int(input()[1:-1])
k=2
while True:
    tmp = n
    while True:
        if tmp%k==1:
            tmp//=k
        else:
            break
    if tmp == 0:
        print(k)
        break
    else:
        k += 1