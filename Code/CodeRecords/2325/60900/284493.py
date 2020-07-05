str = input().split(',')
for i in range(0,len(str)):
    str[i]=int(str[i])

list = list(set(str))
f =[]
for i in range(0,len(list)):
    f.append(str.count(list[i]))
result =True
if min(f)==1:
    result =False
for i in range(2,min(f)+1):
    for j in range(0,len(f)):
        if f[j]%i!=0:
            result = False
    if result ==True:
        break

print(result)