n=int(input())
a=[]
p=[]
for i in range(n):
    ap=input().split(' ')
    a.append(int(ap[0]))
    p.append(int(ap[1]))
left=0
right=0
num=0
while right<n:
    if right + 1 < n and p[right + 1] >= p[left]:
        right+=1
    else:
        num+=p[left]*sum(a[left:right+1])
        right+=1
        left=right
print(num)