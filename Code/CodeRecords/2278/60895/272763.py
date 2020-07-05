t=int(input())
while t>0:
    t=t-1
    n=int(input())
    s=input().split(' ')
    a=[]
    result=[]
    for item in s:
        x=int(item)
        temp=''
        while x>0:
            if x%2==1:
                temp='1'+temp
            else:
                temp='0'+temp
            x=x//2
        a.append(temp)
    for i in range(0,n-1):
        p=a[i]
        q=a[i+1]
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
        result.append(str(num))
    result.append(s[n-1])
    answer=' '.join(result)
    print(answer)