def solve():
    length=int(input().split()[1])
    nums = list(map(int, input().split()))
    res=999
    for num in nums:
        if length%num==0:
            if int(length/num)<res:
                res=int(length/num)
    print(res)
    
if  __name__ == '__main__' :
    solve()