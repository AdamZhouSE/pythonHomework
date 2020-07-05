t=int(input())
while t>0:
    t=t-1
    n,sum=input().split(' ')
    n=int(n)
    sum=int(sum)
    s=input().split(' ')
    len=2
    result=''
    while len<=n:
        for i in range(0,n-len+1):
            temp=s[i:i+len]
            num=0
            for item in temp:
                num=num+int(item)
            if num==sum:
                result=str(i+1)+' '+str(i+len)
        len=len+1
    if result=='':
        result='-1'
    print(result)