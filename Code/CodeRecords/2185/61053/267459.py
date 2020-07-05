def find_k(k):
    lst = ["4","7"]
    if k <= 2:
        return int(lst[k-1])
    index = 0
    L = 2
    while len(lst) < k:
        for i in range(L):
            lst.append("4"+lst[index])
            index += 1
        index -= L
        for i in range(L):
            lst.append("7"+lst[index])
            index += 1
        L *= 2
    return int(lst[k-1])

if __name__ == "__main__":
    testNO = int(input())
    ans = []
    for i in range(testNO):
        n = int(input())
        ans.append(find_k(n))
    for res in ans:
        print(res)