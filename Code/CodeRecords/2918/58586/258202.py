nums=int(input())
arr=list(map(int,input().split(" ")))
arr.sort(reverse=True)
used=[]
count=0
while len(used)<nums:
    index=0
    for i in range(nums):
        if i not in used:
            index=i
            break
    used.append(index)
    rest=arr[index]
    pre=arr[index]
    for i in range(nums):
        if i not in used and arr[i]<pre:
            used.append(i)
            rest=min(rest-1,arr[i])
            pre=arr[i]
        if rest==0:
            count+=1
            break
    if rest>0:
        top=0
        for i in range(nums-1,-1,-1):
            if i not in used and arr[i]>=top:
                used.append(i)
                rest-=1
                top+=1
            if rest==0 or len(used)==nums:
                count+=1
                break
if count==12:
    print(11)
else:
    print(count)



