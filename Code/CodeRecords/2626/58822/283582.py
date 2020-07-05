def com(a):
    if(len(a)==1):
        return [a[0]]
    res=[]
    sum=0
    if(len(a)==2):
        k=a[0]*a[1]+a[1]
        n=a[0]*a[1]+a[0]
        res.append(k)
        res.append(n)
        return res
    for i in range(0,len(a)):
        if(i==0):
            li=com(a[1:len(a)])
            for i in range(len(li)):
                sum=a[0]*a[1]+li[i]
                res.append(sum)
                sum=0
            continue
        if(i!=(len(a)-1) and i!=0):
            li=a[0:i]
            li.extend(a[i+1:len(a)])
            li=com((li))
            sum=0
            for k in range(len(li)):
                sum=li[k]+(a[i]*a[i-1]*a[i+1])
                res.append(sum)
            continue
        if(i==len(a)-1):
            sum=0
            left = com(a[0:(i-1)])
            for k in range(len(left)):
                sum = left[k] +(a[i] * a[i - 1])
                res.append(sum)
    return res

n=input()
li=list(eval(n))
w=com(li)
max=w[0]
for i in range(1,len(w)):
    if(w[i]>max):
        max=w[i]
print(max)