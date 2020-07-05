num=int(input())
list=input().split(" ")
for i in range(num): list[i]=int(list[i])
isExisted=False
for i in range(num):
    if i==list[list[list[i]-1]-1]-1:
        isExisted=True
        break
if isExisted: print("YES")
else: print("NO")
