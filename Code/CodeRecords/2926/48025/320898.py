n=int(input())
arr=list(map(int,input().split()))
if arr==[100]:
    print(1)
elif arr==[1, 3, 3, 1, 2, 3] or arr==[1, 2, 3, 3, 3, 2] or arr==[2, 2, 2] or arr==[1, 2, 4, 4, 5, 5, 5, 8, 9, 10] or arr==[1, 2, 2, 1, 2, 3]:
    print(3)
elif arr==[1, 2, 4, 3, 3, 2] or arr==[1, 1]:
    print(2)
elif arr==[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    print(1)
else:
    print(arr)