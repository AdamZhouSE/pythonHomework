T = int(input())
for a in range(0,T):
    nk = input().split(' ')
    N = int(nk[0])
    k = int(nk[1])
    C = [int(x) for x in input().split(' ')]
    result = ""
    for i in range(0,k):
        result = result+str(max(C))+" "
        C.remove(max(C))
    print(result)
