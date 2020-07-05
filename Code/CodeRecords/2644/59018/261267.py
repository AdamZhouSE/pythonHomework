info=input()[1:-1].split(',')
a=[int(y) for y in info]
K=int(input())
b=[]
for i in range(len(a)-1):
    for j in range(i,len(a)):
        if sum(a[i:j])>=K:
            b.append(j-i)
            break
if len(b)==0:
    print(-1)
else:
    print(min(b))



