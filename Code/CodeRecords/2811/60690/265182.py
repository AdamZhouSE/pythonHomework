coNo=-1
quality=input().split(" ")
p=int(quality[0])
n=int(quality[1])
nums=[]
dict={}

for i in range(n):
    nums.append(int(input()))
for i in range(p):
    dict[i]=-1

isCo=False
index=0
while isCo==False and index<n:
    if dict[nums[index]%p]==-1:
        dict[nums[index]%p]=nums[index]
        coNo+=1
    else:
        isCo=True
        coNo+=1
    index+=1
if isCo==True:
    coNo+=1
else:
    coNo=-1

print(coNo)