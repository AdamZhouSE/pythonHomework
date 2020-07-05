string=str(input())
res=''
for i in range(len(string)):#正序
    res+=string[i]
for i in range(len(string)-1,-1,-1):#反序
    res+=string[i]
print(res)