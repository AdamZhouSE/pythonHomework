n=int(input())
ls=input().split(' ')
ls=[int(ls[i]) for i in range(n)]
#print(ls)
r=[]
for i in range(n-1):
    r.append(ls[i]+ls[i+1])
r.append(ls[n-1])
r=[str(r[i]) for i in range(n)]
s=" ".join(r)
print(s)