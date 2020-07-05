def solve():
    input()
    nums=list(map(int,input().split()))
    allSum=sum(nums)
    odds=list(filter(lambda x:x%2==1,nums))
    evens=list(filter(lambda x:x%2==0,nums))
    odds.sort(reverse=True)
    evens.sort(reverse=True)
    if len(odds)==len(evens):
        print(0)
        return
    if len(odds)>len(evens):
        res=sum(evens)+sum(odds[:len(evens)+1])
        res=allSum-res
        print(res)
        return
    res=sum(odds)+sum(evens[:len(odds)+1])
    res=allSum-res
    print(res)

if  __name__ == '__main__' :
    solve()