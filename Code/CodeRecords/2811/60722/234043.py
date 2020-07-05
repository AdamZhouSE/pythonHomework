a=input().split(" ")
p=int(a[0])
n=int(a[1])
result=-1
num=[]
for i in range(n):
    num.append(int(input()))
Hash=[]
for i in range(p):
    Hash.append(-1)
for i in range(n):
    place=num[i]%p
    if Hash[place]==-1:
        Hash[place]=num[i]
    else:
        result=i+1
        break
print(result)