num=int(input())
list=input().split(" ")
for i in range(num): list[i]=int(list[i])
list.sort()
res=1
for i in range(1,num):
    time=0
    for j in range(0,i):
        time+=list[j]
    if time<=list[i]: res+=1
    else: list[i]=0
print(res)