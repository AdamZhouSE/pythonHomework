list=input()
res=[]
for i in range(len(list)):
    if int(list[i])%2==0:
        res.append(list[i])
for i in range(len(list)):
    if int(list[i]) % 2 == 1:
        res.append(list[i])
print(res)