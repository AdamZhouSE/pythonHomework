n=int(input())
list=[int(i) for i in input().split()]
index=0
for i in range(1,n-1):
    if list[i]<list[i-1] and list[i]<list[i+1]:
        index+=1
    if list[i]>list[i-1] and list[i]>list[i+1]:
        index+=1
print(index)