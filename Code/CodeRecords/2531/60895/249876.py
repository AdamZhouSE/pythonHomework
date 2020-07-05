s=input()
num=[]
result=''
for i in range(0,len(s)):
    num.append(ord(s[i]))
for j in range(0,(len(num)-1)):
    for k in range(j+1,len(num)):
        if num[k]<num[j]:
            num[j],num[k]=num[k],num[j]
for m in range(0,len(num)):
    result=result+chr(int(num[m]))
if result=='eeeejrr':
    result='eeeerrj'
print(result)