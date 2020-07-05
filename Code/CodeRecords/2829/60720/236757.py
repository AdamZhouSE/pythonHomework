size=int(input())
list=input().split()
for i in range(size):
    list[i]=int(list[i])
list.sort()
a=int(list[size-2])-int(list[0])
b=int(list[size-1])-int(list[1])
if a>b:
    print(b)
else:
    print(a)