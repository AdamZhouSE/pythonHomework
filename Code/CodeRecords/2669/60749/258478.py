n=int(input())
res=[]

for _ in range(n):
    res.append(int(input()))
for t in res:
    list1=[]
    for x in range(0,t+1):
        list1.append(x&t)
    list1=sorted(set(list1))[::-1]
    str1=""
    for m in list1:
        str1=str1+str(m)+" "
    print(str1)
