if __name__ == "__main__":
    testNO = int(input())
    for i in range(testNO):
        n,m = map(int,input().split())
        lst = list(map(int,input().split()))
        lst = sorted(lst,reverse=True)
        print(*lst[0:m])