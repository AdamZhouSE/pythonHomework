num=int(input())
list=input().split(" ")
for i in range(num): list[i]=int(list[i])
list.sort()
for i in range(num-1):
    if i%2==0: list.pop(-1)
    else: list.pop(0)
print(list[0])