def solve():
    n=int(input())
    nums=list(map(int,input().split()))
    line=[0 for i in range(n)]

    s=0
    for i in range(n):
        s+=nums[i]
        line[i]=s
        if s==0:
            print("Yes")
            return
        for j in range(i):
            if s-line[j]==0:
                print("Yes")
                return
    print("No")

if  __name__ == '__main__' :
    total=int(input())
    for _ in range(total):
        solve()