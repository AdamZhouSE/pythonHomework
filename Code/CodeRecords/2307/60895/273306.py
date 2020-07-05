t=int(input())
while t>0:
    t=t-1
    n=int(input())
    len=n//2+1
    s=input().split(' ')
    result=-1
    for i in range(0,n-1):
        for j in range(i+1,n):
            if int(s[i])>int(s[j]):
                s[i],s[j]=s[j],s[i]
    for k in range(0,n-len+1):
        if s[k]==s[k+1]:
            temp=s[k:k+len]
            for item in temp:
                if item==s[k]:
                    result=int(s[k])
                else:
                    result=-1
                    break
        if result!=-1:
            break
    print(result)