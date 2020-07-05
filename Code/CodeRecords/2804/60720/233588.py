str=input()
list=str.split("+")
list.sort()
for index in range(len(list)-1):
    print(list[index],end='')
    print('+',end='')
print(list[len(list)-1])