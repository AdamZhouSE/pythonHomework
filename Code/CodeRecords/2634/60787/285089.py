num=eval(input())
k=int(input())
re=[]
for p in range(0,len(num)-1):
    for q in range(p+1,len(num)):
        re.append([num[p],num[q]])
for i in range(0,len(re)):
    for j in range(0,len(re)-1):
        a=(float)(re[j][0]/re[j][1])
        b=(float)(re[j+1][0]/re[j+1][1])
        if a>b:
            re[j],re[j+1]=re[j+1],re[j]
print(re[k-1])