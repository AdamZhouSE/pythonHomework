n=int(input())
list1=input().split()
list1=[int(x) for x in list1]
set1=set(list1)
set1.discard(0)
print(len(set1))