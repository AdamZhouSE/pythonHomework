T = int(input())
while T > 0:
    M, N, k = input().split(" ")
    M = int(M)
    N = int(N)
    k = int(k)
    astr = input().split(" ")
    bstr = input().split(" ")
    string = astr + bstr
    # print(string)
    nstr = [int(string[i]) for i in range(len(string))]
    nstr.sort()
    print(nstr[k - 1])
