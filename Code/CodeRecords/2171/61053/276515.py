def translst(lst,n):
    odd = []
    even = []
    for no in lst:
        if no % 2 == 0:
            even.append(no)
        else:
            odd.append(no)
    even.extend(odd)
    return even

if __name__ == "__main__":
    testNO = int(input())
    ans = []
    for i in range(testNO):
        n = int(input())
        lst = list(map(int,input().split()))
        ans.append(translst(lst,n))
    for res in ans:
        for no in res:
            print(no,end=" ")
        print()