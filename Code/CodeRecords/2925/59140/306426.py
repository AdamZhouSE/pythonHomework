n=int(input())
a=[int(x) for x in input().split(" ")]
b=[int(x) for x in input().split(" ")]
index=0
result=0
for i in range(n):
    if b[i]==a[0]:
        a.remove(b[i])
        index+=1
    else:
        a.remove(b[i])
        result+=1
print(result)