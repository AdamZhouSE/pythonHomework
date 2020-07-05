if __name__ == "__main__":
    testNO = int(input())
    ans = []
    for i in range(0,testNO):
        N = int(input())
        num = list(map(int,input().split()))
        count = 0
        for j in range(0,N-1):
            for k in range(j+1,N):
                if num[j]+num[k] in num:
                    count = count + 1
        if count == 0:
            count = -1
        ans.append(count)
    for res in ans:
        print(res)
