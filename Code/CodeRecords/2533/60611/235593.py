l=str(input())
l=l[1:-1]
l=l.split(',')
result=[]
for i in range(len(l)):
    if int(l[i])%2==0:
        result.append(int(l[i]))
for i in range(len(l)):
    if int(l[i])%2!=0:
        result.append(int(l[i]))
print(result)