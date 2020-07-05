def op(li,s,le):
    s1=s[(li[0]):(li[1])]
    if(li[2]==0):
        s=s1+s
    else:
        if(li[2]==len(s)):
            s=s+s1
        else:
            s=s[0:li[2]]+s1+s[li[2]:len(s)]
    if(len(s)>le):
        s=s[0:le]
    return s
r=input().split(' ')
resnum=int(r[0])
maxnum=int(r[1])
n=input()
num=int(input())
for i in range(num):
    k=input()
    li=k.split(' ')
    for i in range(len(li)):
        li[i]=int(li[i])
    n=op(li,n,maxnum)
print(n[0:resnum])