str=input()
nums=list(map(int,str[1:len(str)-1].split(",")))
size=len(nums)
countA=0
countB=0
a=0
b=0
for i in range(0,size):
    if(countA==0 or a==nums[i]):
        a=nums[i]
        countA+=1
    elif(countB==0 or b==nums[i]):
        b=nums[i]
        countB+=1
    else:
        countA-=1
        countB-=1
countA=0
countB=0
for i in range(0,size):
    if(nums[i]==a):
        countA+=1
    if(nums[i]==b):
        countB+=1
if(countA>size//3 and countB>size//3):
    print([a,b])
elif(countA>size//3):
    print([a])
else:
    print([b])
        