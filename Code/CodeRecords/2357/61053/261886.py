def find_pair(numlst1,numlst2,tar):
    res = []
    for no in numlst1:
        if tar-no in numlst2:
            lst = [no]
            lst.append(tar-no)
            res.append(lst)
    return res

if __name__ == "__main__":
    testNO = int(input())
    ans = []
    for i in range(0,testNO):
        N,M,X = map(int,input().split())
        numlst1 = list(map(int,input().split()))
        numlst2 = list(map(int, input().split()))
        ans.append(find_pair(numlst1,numlst2,X))
    for res in ans:
        for pair in res:
            print(*pair)