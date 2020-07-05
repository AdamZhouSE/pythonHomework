num=int(input())
list=input().split(" ")
for i in range(num):
    list[i]=int(list[i])
list.sort()

if list[-2]-list[0]<list[-1]-list[1]:
    list.pop(-1)
else: list.pop(0)
print(list[-1]-list[0])