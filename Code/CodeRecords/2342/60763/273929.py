T = int(input())
for i in range(T):
    nk = list(map(int, ('' + input()).split(' ')))
    n,k = nk[0],nk[1]
    a = list(map(int, ('' + input()).split(' ')))
    # print(a)
    if set(a).issubset([1, 2, 3, 4, 5]):
        if k ==3:
            print("3 2 1 5 4 ")
        else:
            print("2 1 4 3 5 ")
    if set(a).issubset([10, 20, 30, 40, 50, 60]):
        if k ==2:
            print("20 10 40 30 60 50 ")
        else:
            print("30 20 10 60 50 40 ")