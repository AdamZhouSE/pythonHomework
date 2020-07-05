n=int(input())
list1=input().split()
list1=[int(x) for x in list1]
list1.sort()
print(' '.join(list1))