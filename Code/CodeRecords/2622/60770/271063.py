def solve():
    nums=list(map(int,input().split(',')))

    m,c=-1,0
    for num in nums:
        if num==m:
            c+=1
        else:
            if c==0:
                m,c=num,1
            else:
                c-=1
    if nums.count(m)>len(nums)/2:
        print(m)
    else:
        print(-1)
if  __name__ == '__main__' :
    solve()