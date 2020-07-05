def find_missing(numlst,n):
    lst = []
    for i in range(0,n):
        lst.append(0)
    for num in numlst:
        lst[num-1] = lst[num-1] + 1

    find_A = False
    find_B = False
    ret = []
    for i in range(0,n):
        if lst[i] == 0 and (not find_A):
            find_A = True
            A = i + 1
        if lst[i] > 1 and (not find_B):
            find_B = True
            B = i + 1
        if find_A and find_B:
            break
    if find_A:
        ret.append(B)
        ret.append(A)
    else:
        ret.append(0)
        ret.append(0)
    return ret

if __name__ == "__main__":
    testNO = int(input())
    ans = []
    for i in range(0,testNO):
        n = int(input())
        numlst = list(map(int,input().split()))
        ans.append(find_missing(numlst,n))
    for res in ans:
        print(*res)