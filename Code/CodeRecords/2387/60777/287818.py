temp=[int(x) for x in input().split(' ')]
n=temp[0]
m=temp[1]
temp=[int(x) for x in input().split(' ')]
t=temp.copy()
for i in range(m):
    pre=[int(x) for x in input().split(' ')]
    l=pre[1]
    r=pre[2]
    now=temp[l-1:r]
    if(pre[0]==0):
        now.sort()
    else:
        now.sort(reverse=True)
    temp=temp[:l-1]+now+temp[r:]
        
q=int(input())
print(temp[q-1])