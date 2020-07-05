l=eval(input())
len=len(l)
res=0
for i in range(0,len,2):
    if(l[i]%2==0): #判断当前位置是奇数还是偶数，以确定其情侣的号码
        tmp=l[i]+1
    else:
        tmp=l[i]-1
    if(tmp==l[i+1]):#旁边恰好是其情侣
        continue
    for j in range(i+2,len):
        if(tmp==l[j]):
            l[i+1],l[j]=l[j],l[i+1]
            res+=1
print(res)