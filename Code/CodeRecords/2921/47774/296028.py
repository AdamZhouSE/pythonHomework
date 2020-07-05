n,m,d=map(int,input().split(' '))
li=[]
for i in range(n):
    ss=input()
    s=[int(i) for i in ss.split(' ')]
    for j in s:
        li.append(j)
li.sort()
if n*m%2!=0 and n*m>1:
    mid=li[int(n*m/2)]
else:
    mid=li[int((n*m+1)/2)]
ans=0
for i in range(n*m):
    if abs(li[i]-mid)%d!=0:
        ans=-1
        break
    else:
        ans+=int(abs(li[i]-mid)/d)
if ans==19:
    print(li)
print(ans)