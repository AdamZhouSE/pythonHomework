n=int(input())
names=[]
output=[]
for i in range(n):
    names.append(input())
    setNames=set(names)
    if names.__len__()>setNames.__len__():
        output.append("YES")
    else:
        output.append("NO")
for i in output:
    print(i)