ex=int(input())
while ex>0:
    ex -= 1
    idx,result=0,0
    n=int(input())
    nums=list(map(int,input().split()))
    store=False
    box=[]
    while idx<n-1:
        if nums[idx]>=nums[idx+1]:
            store=True
            box.append(nums[idx])
        elif store==True:
            box.append(nums[idx])
            box.append(nums[idx+1])
            result += min(box[0],box[-1])*(len(box)-2)
            del box[0]
            del box[1]
            result -= sum(box)
            box=[]
            store=False
        idx += 1
    print(result)