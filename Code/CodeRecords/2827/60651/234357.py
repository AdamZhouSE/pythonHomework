n=int(input())
list1=input().split()
list1=[int(x) for x in list1]
list1.sort()
list1=[str(x) for x in list1]
print(' '.join(list1))