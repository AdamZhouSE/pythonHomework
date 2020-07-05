nums=eval(input())
maxlen=0
length=len(nums)
for start in range(0,length):
    current=1
    for i in range(start,length-1):
        if nums[i]>=nums[i+1]:
            break
        else:
            current+=1
    if current>maxlen:
        maxlen=current
print(maxlen)