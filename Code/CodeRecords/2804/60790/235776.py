list1=input().split("+")
list1.sort()
list2=list1[0:-1]

for letter in list2:
    print(letter+"+",end='')
print(list1[-1])