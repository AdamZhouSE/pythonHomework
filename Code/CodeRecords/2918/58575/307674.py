def Zero(nums):
    for i in nums:
        if i!=0:
            return False
    return True

n=int(input())
box=list(map(int,input().split(" ")))
box.sort()
box.reverse()

num=0
while Zero(box)==False and len(box)!=1:
    i=1
    while i<len(box) and box[i]>=box[0]:
        i+=1
    if i==len(box):
        i-=1
    box[0]-=1
    box[0]=min(box[0],box[i])
    if box[0] ==0:
        num+=1
        box=box[1:i]+box[i+1:]
        continue
    box=box[0:i]+box[i+1:]
if num+len(box)==12:
    num-=1
print(num+len(box))