def solve():
    n,k=map(int,input().split())
    nums=list(map(int,input().split()))
    nl=[]
    for num in nums:
        if nums.count(num)==1:
            nl.append(num)

    if k>len(nl):
        print(-1)
    else:
        print(nl[k-1])

if  __name__ == '__main__' :
    total=int(input())
    for _ in range(total):
        solve()