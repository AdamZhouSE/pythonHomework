def solve():
    total=int(input())
    nums = list(map(int, input().split()))
    indexs=list(range(1,10))
    vs=list(zip(indexs,nums))
    least=min(nums)
    most=nums.index(least)+1
    bits=int(total/least)
    if bits==0:
        print(-1)
        return
    res=[most for i in range(bits)]
    rest=total%least
    for i in range(bits):
        rest+=nums[res[i]-1]
        available=list(filter(lambda x:x[1]<=rest,vs))
        if len(available)==0:
            break
        instead=max(map(lambda x:x[0],available))
        res[i]=instead
        rest-=nums[instead-1]
    res=list(map(lambda x:str(x),res))
    print(''.join(res))

if  __name__ == '__main__' :
    solve()