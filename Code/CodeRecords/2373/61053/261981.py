def max_value(lst):
    if len(lst) == 1:
        return lst[0]
    if len(lst) == 2:
        return max(lst[0],lst[1])

    best = []
    best.append(lst[0])
    best.append(max(lst[0],lst[1]))
    for i in range(2,len(lst)):
        best.append(max(best[i-1],best[i-2]+lst[i]))
    return best[-1]

if __name__ == "__main__":
    testNO = int(input())
    ans = []
    for i in range(0,testNO):
        N = int(input())
        lst = list(map(int,input().split()))
        ans.append(max_value(lst))
    for res in ans:
        print(res)