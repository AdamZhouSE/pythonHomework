T  = int(input())
for i in range(T):
    numList = [int(x) for x in input().split()]
    N,L,R = numList[0],numList[1],numList[2]
    Str = list(bin(N)[2:])
    Str.reverse()
    # print(Str)
    for j in range(L-1,R):
        Str[j] = '1'
    Str.reverse()
    print(int("".join(Str),2))