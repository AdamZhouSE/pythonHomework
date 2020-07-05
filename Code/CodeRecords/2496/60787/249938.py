s=sorted(list(input()))
temp=[s[0]]
rest=[]
for i in range(1,len(s)):
    if s[i]==temp[-1]:
        temp.append(s[i])
    else:
        rest.append(temp)
        temp=[s[i]]
    if i==len(s)-1:
        rest.append(temp)
max_num=0
max_index=0
for i in range(0,len(rest)):
    if len(rest[i])>max_num:
        max_num=len(rest[i])
        max_index=i
temp=rest[max_index]
re=[]
for i in range(0,len(rest[max_index])):
    re.append([rest[max_index][i]])
del rest[max_index]
remain=[]
for i in range(0,len(rest)):
    for j in range(len(rest[i])):
        remain.append(rest[i][j])
if len(remain)<max_num-1:
    print("")
else:
    current=0
    for i in range(0,len(remain)):
        re[current%len(re)].append(remain[i])
        current+=1
    result=""
    for i in range(0,len(re)):
        result=result+"".join(re[i])
    print(result)