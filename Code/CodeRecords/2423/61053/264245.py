if __name__ == "__main__":
    testNO = int(input())
    ans = []
    for i in range(testNO):
        m,n = map(int,input().split())
        set1 = set(input().split())
        set2 = set(input().split())
        if set2.issubset(set1):
            ans.append(True)
        else:
            ans.append(False)
    for res in ans:
        if res:
            print('Yes')
        else:
            print("No")