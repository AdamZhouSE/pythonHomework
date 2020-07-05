def solve():
    input()
    nums = input().split()
    nums.reverse()
    snum=set(nums)
    numAndIndex=list(map(lambda x:[x,nums.index(x)],snum))
    numAndIndex.sort(key=lambda x:x[1])
    res=list(map(lambda x:x[0],numAndIndex))
    res.reverse()
    print(len(res))
    print(" ".join(res))


if  __name__ == '__main__' :
    solve()