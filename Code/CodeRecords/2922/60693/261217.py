def can_done(arr):
    dif_nums=set(arr)
    if len(dif_nums)>3:
        return False
    if len(dif_nums)<3:
        return True
    else:
        dif_nums=sorted(dif_nums)
        if (dif_nums[0]+dif_nums[2])%2==0 and (dif_nums[0]+dif_nums[2])//2==dif_nums[1]:
            return True
n=int(input())
arr=list(map(int,input().split()))
res=can_done(arr)
if res:print('YES')
else:print('NO')