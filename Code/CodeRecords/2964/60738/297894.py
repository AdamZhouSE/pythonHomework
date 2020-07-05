def func(a,b):
    lena=len(a)
    lenb=len(b)
    list=[]
    for i in range(lenb+1):
        list.append([])
        for j in range(lena+1):
            list[i].append(0)
    for i in range(1,lena+1):
        list[0][i]=i
    for i in range(1,lenb+1):
        list[i][0]=i
    for i in range(1,lenb+1):
        for j in range(1,lena+1):
            if(a[j-1]==b[i-1]):
                list[i][j] = min(min(list[i - 1][j] + 1, list[i][j - 1] + 1),
                                 list[i-1][j-1]);
            else:
                list[i][j] = min(min(list[i - 1][j] + 1, list[i][j - 1] + 1),
                                 (list[i-1][j-1]+1));
    return list[lenb][lena]

num=int(input())
anslist=[]
for i in range(8):
    anslist.append(0)
list=[]
for i in range(num):
    list.append(input())
for i in range(num-1):
    for j in range(i+1,num):
        mid=func(list[i],list[j])
        if(mid<=8):
            if(mid>0):
                anslist[mid-1]+=1
for i in range(8):
    anslist[i]=str(anslist[i])
ans=" ".join(anslist)
print(ans,"",end="")
