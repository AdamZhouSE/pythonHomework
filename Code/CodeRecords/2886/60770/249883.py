def solve():
    input()
    nums = list(map(int, input().split()))
    socks=set()
    current=0
    res=0
    for num in nums:
        if num in socks:
            socks.remove(num)
            current-=1
        else:
            socks.add(num)
            current+=1
        if current>res:
            res=current
    print(res)

if  __name__ == '__main__' :
    solve()