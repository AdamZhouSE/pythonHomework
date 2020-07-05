def Joseph(n,k):
    lst = []
    for i in range(n):
        lst.append(i)
    count = 0
    index = 0
    while count < n - 1:
        index = (index + k - 1) % (n - count)
        del lst[index]
        count += 1
    return lst[0]+1

if __name__ == "__main__":
    testNO = int(input())
    ans = []
    for i in range(testNO):
        n,k = map(int,input().split())
        ans.append(Joseph(n,k))
    for res in ans:
        print(res)