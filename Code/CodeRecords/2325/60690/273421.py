s=input().split(",")
if len(s)==1 and len(s)==0:print(False)
else:
    nums=s
    dict={}
    for i in range(len(nums)):
        nums[i]=int(nums[i])
        if nums[i] not in dict.keys():
            dict[nums[i]]=1
        else:
            dict[nums[i]]+=1
    base=min(dict.values())
    res=True
    for e in dict.values():
        if e%base!=0:
            res=False
            break
    if base<2: res=False
    print(res)