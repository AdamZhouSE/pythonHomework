nums=list(eval(input()))
rec=1
for i in range(1,max(nums)):
    count=0
    for j in range(len(nums)):
        if nums[j]>=i:
            count+=1
        if count>i:
            rec=i       
            break
    if count==i:
        print(count)
        exit()
print(rec)
