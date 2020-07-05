def move_back(lst):
    res  = []
    count = 0
    for i in lst:
        if i != 0:
            res.append(i)
        else:
            count = count + 1
    for i in range(0,count):
        res.append(0)
    return res

if __name__ == "__main__":
    testNO = int(input())
    ans = []
    for i in range(testNO):
        n = int(input())
        lst = list(map(int,input().split()))
        ans.append(move_back(lst))
    for res in ans:
        for num in res:
            print(num,end=" ")
        print()