num=int(input())
list=input().split()

for i in range(num): list[i]=int(list[i])

list.sort()

for i in range(num-1):
    print(str(list[i])+" ",end="")
print(list[-1])