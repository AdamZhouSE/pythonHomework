nm=input().split(' ')
n=int(nm[0])
m=int(nm[1])
l=[[] for x in range(n)]
for i in range(m):
    action=input().split(' ')
    c=int(action[0])
    a=int(action[1])
    b=int(action[2])
    if c==1:
        for j in range(a-1,b):
            l[j].append(i)
    else:
        ans=[]
        for j in range(a - 1, b):
            ans.extend(l[j])
        print(len(set(ans)))