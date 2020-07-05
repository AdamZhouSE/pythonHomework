def cal(a):
    s=''
    while(a!=0):
        if a%2==1:
            s='1'+s
        else:
            s='0'+s
        a=a//2
    return s
t=int(input())
for i in range(t):
    li=input().split()
    M=int(li[0])
    N=int(li[1])
    s1=cal(M)
    s2=cal(N)
    if len(s1)>len(s2):
        for j in range(len(s1)-len(s2)):
            s2='0'+s2
    elif len(s2)>len(s1):
        for j in range(len(s2)-len(s1)):
            s1='0'+s1
    s1=s1[::-1]
    s2=s2[::-1]
    ind=len(s1)+1
    for j in range(len(s1)):
        if s1[j]!=s2[j]:
            ind=j+1
            break
    if ind==len(s1)+1:
        print('-1')
    else:
        print(ind)