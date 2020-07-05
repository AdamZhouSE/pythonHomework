nums=input()[1:-1]
afterNum=list()
num=0
numberOfnum=0
i=1
while i<len(nums):
    j=i
    while nums[i]!=']':
        i=i+1
    temp=list(map(int,nums[j:i].split(",")))
    afterNum.append(temp)
    num=num+1
    numberOfnum=numberOfnum+len(temp)
    i=i+3
res=list()
i=0
while i<numberOfnum:
    minimum=afterNum[0][0]
    j=0
    while j<num:
        minimum=min(minimum,afterNum[j][0])
        j=j+1
    res.append(minimum)
    j=0
    while j<num:
        if minimum in afterNum[j]:
            afterNum[j].remove(minimum)
            if len(afterNum[j])==0:
                num=num-1
                afterNum.remove(afterNum[j])
            break
        j=j+1
    i=i+1
print(res)