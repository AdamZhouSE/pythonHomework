n=int(input())
a=[]
b=[]
for i in range(n):
    x=input().rstrip()
    a=[]
    for j in range(len(x)):
        a.append(x[j])
    a.sort()
    b.append(a)
b.sort()
#print(b)
sum=1
for i in range(1,len(b)):
    if b[i]!=b[i-1]:
        sum+=1
print(sum,end="")