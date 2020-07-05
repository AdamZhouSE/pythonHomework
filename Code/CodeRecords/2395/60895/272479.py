t=int(input())
while t>0:
    t=t-1
    n=int(input())
    s=input().split(' ')
    for i in range(0,n):
        s[i]=int(s[i])
    for j in range(0,n-1):
        if s[j]==s[j+1]:
            s[j],s[j+1]=2*s[j],0
    temp1=''
    temp2=''
    for item in s:
        if int(item)==0:
            temp2=temp2+'0'+' '
        else:
            temp1=temp1+str(item)+' '
    result=temp1+temp2
    result=result.rstrip(' ')
    print(result)
        