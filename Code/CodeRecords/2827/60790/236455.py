n=input()
list1=input().split()
list1=list(map(int,list1))
list1.sort()
list2=list1[0:-1]
for num in list2:
    print(str(num)+" ",end='')
print(list1[-1])