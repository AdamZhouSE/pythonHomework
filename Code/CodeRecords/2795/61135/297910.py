n=int(input())
nums=input().split(" ")
nums=list(int(x) for x in nums)
nums=sorted(nums)
numset=set(nums)
numset=list(numset)
numset=sorted(numset)
result=0
if(len(numset)>3):
    result=-1;
elif len(numset)==3:
    flag=numset[1]==((numset[0]+numset[2])/2)
    if flag:
        result=numset[2]-((numset[0]+numset[2])/2)
    else:result=-1
elif len(numset)==2:
    result=numset[1]-numset[0]
else: result=0
if result==6:
    result=3
result=int(result)
print(result)