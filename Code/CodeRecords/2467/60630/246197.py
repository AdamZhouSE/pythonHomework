Times = int(input(""))

while Times > 0 :
    Times -= 1
    m, n, k = [int(p) for p in input("").split(' ')]
    numA = [int(p) for p in input("").split(' ')]
    numB = [int(p) for p in input("").split(' ')]
    i1 = 0 ; i2 = 0
    while True :
        k -= 1
        if numA[i1] <= numB[i2] :
            if k <= 0 :
                print(numA[i1])
                break
            i1 += 1
        else :
            if k <= 0 :
                print(numB[i2])
                break
            i2 += 1
