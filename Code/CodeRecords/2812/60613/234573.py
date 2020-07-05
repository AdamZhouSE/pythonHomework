NUM=int(input())
lst=input().split()

lst=list(map(int,lst))

lst=set(lst)
if 0 in lst:
    print(len(lst)-1)
else:
    print(len(lst))