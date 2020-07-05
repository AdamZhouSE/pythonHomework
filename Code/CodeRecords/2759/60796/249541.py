n=int(input())
result=[]
ls=[]
while n>0:
    s=input()
    ls.append(s.split(" "))
    ls[len(ls)-1]=[int(x) for x in ls[len(ls)-1]]
    n=n-1
#print(ls

for i in range(len(ls)):
    m=ls[i][0]
    n=ls[i][1]
    a=ls[i][2]
    b=ls[i][3]
    total=0
    for j in range(m,n+1):
        if j%a==0 or j%b==0:
            total=total+1
    result.append(total)
for i in range(0,len(result)):
    print(result[i])
