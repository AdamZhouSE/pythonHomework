if __name__ == "__main__":
    testNO = int(input())
    for i in range(testNO):
        n,m = map(int,input().split())
        lst = list(map(int,input().split()))
        lst = sorted(lst,reverse=True)
        for j in range(0,m):
            print(lst[j],end=" ")
        print()