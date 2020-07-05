n=int(input())
result=[]
while n>0:
    this=int(input())
    if this%5==0:
        result.append("YES")
    else:
        result.append("NO")
    n=n-1
for i in range(len(result)):
    print(result[i])
    