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

def trans(list,n):
    for i in range(n-1):
        if list[i]==list[i+1] and list[i]!=0:
            list[i] = list[i] * 2
            list[i+1] = 0
    return move_back(list)

if __name__ == "__main__":
    testNO = int(input())
    ans = []
    for i in range(testNO):
        n = int(input())
        lst = list(map(int,input().split()))

        ans.append(trans(lst,n))

    for res in ans:
        print(*res)