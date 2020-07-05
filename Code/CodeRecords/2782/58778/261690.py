n=int(input())
temp=[]
re=[]
for i in range(n):
    m=int(input())
    if(len(temp)==0):
        temp.append(m)
        re.append(m)
    else:
        temp.append(m)
        c=[]
        for j in range(len(temp)-1):
            c.append(abs(m-temp[j]))
        re.append(min(c))
    #print(re)
    #print(temp)
print(sum(re),end='')