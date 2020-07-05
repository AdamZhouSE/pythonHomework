n=int(input())
s=input()
w=input().rstrip(' ').split(' ')
W=[]
maxval=0
for item in w:
    temp=int(item)
    tempstr=''
    while temp>0:
        if temp%2==1:
            tempstr='1'+tempstr
        else:
            tempstr='0'+tempstr
        temp=temp//2
    W.append(tempstr)
for i in range(0,n-1):
    sa=s[i:n]
    for j in range(i+1,n):
        sb=s[j:n]
        preval=0
        for k in range(0,len(sb)):
            if sa[k]==sb[k]:
                preval=preval+1
            else:
                break
        p=W[i]
        q=W[j]
        xor=''
        if len(p)>len(q):
            q='0'*(len(p)-len(q))+q
        else:
            p='0'*(len(q)-len(p))+p
        for i in range(0,len(p)):
            if p[i]==q[i]:
                xor=xor+'0'
            else:
                xor=xor+'1'
        index=1
        num=0
        for j in range(0,len(xor)):
            if xor[len(xor)-1-j]=='1':
                num=num+index
            index=index*2
        val=num
        sumval=val+preval
        if sumval>maxval:
            maxval=sumval
print(maxval)