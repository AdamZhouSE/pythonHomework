NUM=int(input())
data=[input().split()[0] for i in range(NUM)]
result=[]
for i in range(len(data)):
    l=list(data[i])
    l.sort()
    result.append("".join(l))

result=set(result)
print(len(result),end="")
