def find_sum(lst,tar,n):
    if n == 0:
        return -1
    i = j = 0
    cur_sum = lst[0]
    while 1:
        if cur_sum > tar:
            i = i + 1
            if i == n:
                return -1
            if j < i:
                j = i
                cur_sum = lst[i]
            else:
                cur_sum = cur_sum - lst[i-1]
        elif cur_sum < tar:
            j = j + 1
            if j == n:
                return -1
            cur_sum = cur_sum + lst[j]
        else:
            res = [i+1]
            res.append(j+1)
            return res

if __name__ == "__main__":
    testNO = int(input())
    ans = []
    for i in range(testNO):
        N,tar = map(int,input().split())
        numlst = list(map(int,input().split()))
        ans.append(find_sum(numlst,tar,N))
    for res in ans:
        if res == -1:
            print(-1)
        else:
            print(*res)