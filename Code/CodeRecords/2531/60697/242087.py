str=input()
tmp={}
for i in str:
    if(i not in tmp.keys()):
        tmp[i]=1
    else:
        tmp[i]=tmp[i]+1
tmp=sorted(tmp.items(),key=lambda x:x[1],reverse=True)
a=""
for j in range(len(tmp)):
    for k in range(tmp[j][1]):
        a=a+tmp[j][0]
print(a)