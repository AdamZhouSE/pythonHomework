def func(s,n):
    ans=[]
    for i in range(0,n-1):
        for j in range(i+1,n):
            if s[j]>s[i]:
                ans.append((s[i]) * (j - i))
            else:
                ans.append((s[j]) * (j - i))
    ans=sorted(ans,reverse=True)
    return ans[0]


n = int(input())
ans = []
for i in range(0, n):
    m=int(input())
    k=input()
    s=k.split(" ")
    temp=[]
    for j in range(0,m):
        temp.append(s[j])
    tem=list(map(int,temp))
    ans.append(func(tem,m))

    '''if k!="1 5 4 3 "or k!="3 1 2 4 5"
        print(m)
        print(s)'''

for i in ans:
    print(i)