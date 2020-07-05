length,times=input().split(' ')
length=int(length)
times=int(times)
s=input().split(' ')
while times>0:              
    times=times-1
    op,l,r=input().split(' ')
    op=int(op)
    l=int(l)
    r=int(r)
    if op==0:
        for i in range(l-1,r-1):
            for j in range(i+1,r):
                if int(s[i])>int(s[j]):
                    s[i],s[j]=s[j],s[i]
    else:
        for i in range(l-1,r-1):
            for j in range(i+1,r):
                if int(s[i])<int(s[j]):
                    s[i],s[j]=s[j],s[i]
q=int(input())
print(s[q-1])