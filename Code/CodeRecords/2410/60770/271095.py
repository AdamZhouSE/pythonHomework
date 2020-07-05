def solve():
    nums=list(map(int,input().split(',')))
    dif=int(input())
    mem,res={},1
    for i in nums:
        if i-dif in nums:
            mem[i]=mem[i-dif]+1
        else:
            mem[i]=1
    res=max(mem)
    print(res)

if  __name__ == '__main__' :
    solve()