def cal(l1):
    t=[]
    sum=0
    for i in range(n):
        t=[]
        sum+=1
        for j in range(0,len(l1),2):
            if sum%2==1:
                t.append(l1[j]|l1[j+1])
            else:
                t.append(l1[j]^l1[j+1])
        l1=t[::]
    return l1[0]
l=eval('['+input().replace(' ',',')+']')
n=l[0]
m=l[1]
l=eval('['+input().replace(' ',',')+']')
for i in range(m):
    s=eval('['+input().replace(' ',',')+']')
    l[s[0]-1]=s[1]
    print(cal(l))