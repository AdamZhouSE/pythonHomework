str=list(input())
max=0
for i in range(0,len(str)):
    temp=[]
    for j in range(i,len(str)):
        if str[j] in temp:
            if len(temp)>max:
                max=len(temp)
                break
        else:
            temp.append(str[j])
print(max)