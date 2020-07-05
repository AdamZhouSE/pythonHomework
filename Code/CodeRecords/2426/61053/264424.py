def find_max_prod(lst,n):
    lst = sorted(lst,reverse=True)
    return max(lst[0]*lst[1]*lst[2],lst[0]*lst[-1]*lst[-2])



if __name__ == "__main__":
    testNO = int(input())
    ans = []
    for i in range(testNO):
        n = int(input())
        lst = list(map(int,input().split()))
        ans.append(find_max_prod(lst,n))
    for res in ans:
        print(res)