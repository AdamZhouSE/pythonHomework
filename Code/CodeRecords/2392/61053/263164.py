def find_prod(lst,tar):
    factors = []
    for no in lst:
        if tar % no == 0:
            if tar/no in factors:
                return True
            else:
                factors.append(no)
    return False

if __name__ == "__main__":
    testNO = int(input())
    ans = []
    for i in range(testNO):
        N,tar = map(int,input().split())
        lst = list(map(int,input().split()))
        ans.append(find_prod(lst,tar))
    for res in ans:
        if res:
            print("Yes")
        else:
            print("No")