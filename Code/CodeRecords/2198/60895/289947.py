n=int(input())
s=input()
w=input().split(' ')
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
        