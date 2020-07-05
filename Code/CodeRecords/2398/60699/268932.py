list1=list(map(int,input().split(' ')))
tMax=list1[1]
cnt=list1[0]
nums=[]
for i in range(cnt):
    nums.append(int(input()))
for length in range(1,1000000000):
    cur=tMax
    temp=[]
    for j in range(length):
        temp.append(nums[j])
    temp.sort(reverse=True)
    cur-=temp[length-1]
    for j in range(length):
        temp[j]-=temp[length-1]
    temp.pop()
    index=length
    if cur<0:
        continue
    while index<len(nums):
        temp.append(nums[index])
        temp.sort(reverse=True)
        cur -= temp[length - 1]
        for j in range(length):
            temp[j] -= temp[length - 1]
        temp.pop()
        if cur<0:
            break
        index+=1
    if len(temp)>0:
        cur-=temp[0]
    if cur>=0:
        print(length)
        break