import functools as ft
nums=int(input())
for i in range(nums):
    num=int(input())
    arr=list(map(int,input().split(" ")))
    def compare(x,y):
        if x==y:
            return 0
        elif arr.count(x)>arr.count(y):
            return -1
        elif arr.count(x)<arr.count(y):
            return 1
        else:
            if x<y:
                return -1
            else:
                return 1
    print(*sorted(arr,key=ft.cmp_to_key(compare)),end=' ')
    print()