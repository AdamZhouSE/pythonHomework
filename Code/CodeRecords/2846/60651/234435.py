n=int(input())
list1=input().split()
list1=[int(x) for x in list1]
list1.remove(0)
set1=set(list1)
print(len(set1))