l=input().split(" ")
p=int(l[0])
n=int(l[1])
list=[]
for x in range(n):
    list.append(int(input()))
result=-1
Hash=[]
for y in range(p):
    Hash.append(-1)
for x in range(n):
    num=list[x]%p
    if Hash[num]==-1:
        Hash[num]=list[x]
    else:
        result=x+1
        break
print(result)