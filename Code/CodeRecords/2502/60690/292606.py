n=int(input())
list=[]
for i in range(n):
    list.append(int(input()))

res=0
for i in range(0,len(list)-1):
    res+=max(list[i],list[i+1])
print(res)
