str=list(input()[::-1])
str=list(map(lambda x:"I"if x=="D" else "D",str))
n=len(str)
alist=list(range(n+1))
rlist=[]
for i in range(n):
    count=0
    for c in str[i:]:
        if c=="I":
            count+=1
    rlist.append(alist[len(alist)-1-count])
    del alist[len(alist)-1-count]
    sorted(alist)
rlist.append(alist[0])
rlist.reverse()
print(rlist)