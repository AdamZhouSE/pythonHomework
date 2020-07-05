a=list(eval(input()))
num=[]
for i in range(2**len(a)):
    temp=[]
    for j in range(0,len(a)):
        if (i>>j)%2==1:
            temp.append(a[j])
    num.append(temp)
re=0
for i in range(0,len(num)):
    if len(num[i])>1:
        re+=(max(num[i])-min(num[i]))
print(re)