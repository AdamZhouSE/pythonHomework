def nums(string):
    num='0123456789'
    nums=[]
    i=0
    while i<len(string):
        midstring=''
        k=0
        for j in range(i,len(string)):
            if string[j] in num:
                midstring+=string[j]
                k=k+1
            else:
                break
        if midstring!='':
            nums.append(int(midstring))
            midstring=''
            i=i+k
        else:
            i=i+1
            continue
    return nums

n=input()
a=input()
a=nums(a)
a=sorted(a)
record=[]
i=0
while i <len(a)-1:
    if a[i]!=0:
        a[i+1]=a[i+1]-a[i]
        i=i+1
    else:
        if (i+1)!=len(a)-1:
            record.append(i+1)
            i=i+1
a[0]=0
for v in record:
    a[v]=0
if a[-1]==0 and min(a)>=0:
    print('YES')
else:
    print('NO')