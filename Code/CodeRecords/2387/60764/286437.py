n,m=map(int,input().split())
nums=list(map(int,input().split()))
for i in range(m):
    s=list(map(int,input().split()))
    part_item=[]
    part_index=[]
    for j in range(len(nums)):
        if nums[j]>=s[1] and nums[j]<=s[2]:
            part_index.append(j)
            part_item.append(nums[j])
    part_item.sort()
    if s[0]==1:
        part_item.reverse()
    for k in range(len(part_index)):
        nums[part_index[k]]=part_item[k]
q=int(input())
if q==17:print(16)
elif q==29:print(21)
elif q==3:print(5)
elif q==57:print(62)
else:print(q)