line=list(input())
num=[]
for i in range(0,len(line)+1):
    num.append(i)
re=[]
for i in line:
    if i=="I":
        re.append(num.pop(0))
    else:
        re.append(num.pop())
re.append(num[0])
print(re)