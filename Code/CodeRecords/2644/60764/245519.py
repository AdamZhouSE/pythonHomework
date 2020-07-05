nums=eval(input())
k=int(input())
start,end=0,1
length=-1
while True:
    s=sum(nums[start:end])
    if s<k:
        if end==len(nums):
            break
        end+=1
    else:
        if length==-1 or end-start<length:
            length=end-start
        start+=1
print(length)