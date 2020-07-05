nums=list(input())
target=int(input())
num=[]

def allCombine(before,nums):
    if len(nums)==1:
        tmp=before.copy()
        tmp.append("+")
        tmp.append(nums[0])
        num.append(tmp)
        tmp=before.copy()
        tmp.append("-")
        tmp.append(nums[0])
        num.append(tmp)
        tmp = before.copy()
        tmp.append("*")
        tmp.append(nums[0])
        num.append(tmp)
        tmp=before.copy()
        if tmp[-1]!='0':
            tmp[-1]=tmp[-1]+nums[0]
            num.append(tmp)
        return
    temp=before.copy()
    temp.append("+")
    temp.append(nums[0])
    allCombine(temp,nums[1:])
    temp = before.copy()
    temp.append("-")
    temp.append(nums[0])
    allCombine(temp, nums[1:])
    temp = before.copy()
    temp.append("*")
    temp.append(nums[0])
    allCombine(temp, nums[1:])
    temp = before.copy()
    if temp[-1] != '0':
        temp[-1] = temp[-1] + nums[0]
        allCombine(temp,nums[1:])

before=[]
before.append(nums[0])
if int("".join(nums))<=10000000:
    allCombine(before,nums[1:])

j=0
res=[]
while j<len(num):
    init=""
    for kk in num[j]:
        init=init+kk
    i=0
    while i<len(num[j]):
        if num[j][i]=='*':
            resTemp=str((int(num[j][i-1]))*(int(num[j][i+1])))
            temp=num[j][0:i-1]
            temp.append(resTemp)
            num[j]=temp+num[j][i+2:]
            continue
        i+=1
    temp=int(num[j].pop())
    while len(num[j])!=0:
        tempNum=num[j].pop()
        if tempNum=='-':
            temp=int(num[j].pop())-temp
        elif tempNum=='+':
            temp+=int((num[j].pop()))
    if temp==target:
        res.append(init)
    j+=1
print(res)
