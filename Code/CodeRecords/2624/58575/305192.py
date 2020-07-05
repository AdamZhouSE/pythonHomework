res=[]
nums=input()

def calcu(num,char):
    if len(char)==0:
        return [num[0]]
    if len(char)==1:
        if char[0]=='+':
            return [num[0]+num[1]]
        elif char[0] == '-':
            return [num[0]-num[1]]
        elif char[0] == '*':
            return [num[0] * num[1]]
    listResTemp=[]
    i=0
    while i<len(char):
        left=calcu(num[0:i+1],char[0:i])
        right=calcu(num[i+1:],char[i+1:])
        for k in left:
            for j in right:
                if char[i] == '+':
                    listResTemp.append(k+j)
                elif char[i] == '-':
                    listResTemp.append(k-j)
                elif char[i] == '*':
                    listResTemp.append(k*j)
        i+=1
    return listResTemp

num=[]
char=[]
i=0
while i<len(nums):
    j=i
    while j<len(nums) and nums[j]!='+' and nums[j]!='-' and nums[j]!='*':
        j+=1
    if j<len(nums):
        char.append(nums[j])
    number=int(nums[i:j])
    num.append(number)
    i=j+1
res=calcu(num,char)
print(res)
