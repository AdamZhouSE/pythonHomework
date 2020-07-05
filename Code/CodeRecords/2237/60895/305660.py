m,t=input().split(' ')
m=int(m)
t=int(t)
s=[]
for i in range(1,m+1):
    s.append(str(i))
while t>0:
    t=t-1
    l,r=input().split(' ')
    l=int(l)
    r=int(r)
    part1=s[0:l-1]
    part2=s[l-1:r]
    part3=s[r:m]
    part2.reverse()
    s=part1+part2+part3
result=' '.join(s)
print(result,end=' ')