number=int(input())
list=input().split()
for i in range(number):
    list[i]=int(list[i])
list.sort()
for i in range(number-1):
    print(list[i],end=' ')
print(list[number-1])