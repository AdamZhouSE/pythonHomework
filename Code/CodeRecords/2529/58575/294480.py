def isMi(num):
    flag=True
    while num!=1:
        if num%2!=0:
            flag=False
            break
        num=num//2
    return flag

global nums
nums=list()

def AllCombine(before,str):
    if len(str)==1:
        judge=before+str
        if(judge[0]!='0'):
            judge=int(judge)
            nums.append(judge)
    i=0
    while i<len(str):
        if str[i] in str[0:i]:
            i=i+1
            continue
        AllCombine(before+str[i],str[0:i]+str[i+1:])
        i=i+1

n=input()
AllCombine("",n)
i=0
flag=False
while i<len(nums):
    flag=isMi(nums[i])
    if flag==True:
        break
    i=i+1
if flag==True:
    print("true")
else:
    print("false")