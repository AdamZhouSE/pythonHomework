list2=input()
m=0
n=0
k=0
t=0
for i in range(len(list2)):
    if list2[i]=='[':
        m=i
    if list2[i]==']':
        n=i
    if list2[i]=='k':
        k=i
    if list2[i]=='t':
        t=i
str1=[]
str2=[]
str3=[]
for i in range(len(list2)):
    if i>m and i<n:
        str1.append(list2[i])
    if i>k and i<t:
        str2.append(list2[i])
    if i>t :
        str3.append(list2[i])
def num(list):
    str=[]
    k=1
    temp=[]
    res=[]
    for i in range(len(list)):
        if list[i] == ',' or list[i] == ' ' or list[i] == '=':
            k = 0
            if (len(temp) != 0):
                strr = "".join(temp)
                res.append(strr)
            temp = []
        else:
            temp.append(list[i])
        if i==len(list)-1:
            if (len(temp) != 0):
                strr = "".join(temp)
                res.append(strr)
    return res

list=num(str1)
a=int(num(str2)[0])
b=int(num(str3)[0])
def contains(nums, k, t) -> bool:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if abs(int(nums[i]) - int(nums[j])) <= t and j - i  <= k:
                    return True
        return False
if contains(list,a,b):
    print('true')
else:
    print('false')