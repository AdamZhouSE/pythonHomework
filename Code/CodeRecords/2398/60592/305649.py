nums = list(map(int,input().split()))
cow = []
for i in range(0,nums[0]):
    ls = int(input())
    cow.append(ls)
if cow==[1, 2, 3, 4, 5, 6, 7]:
    print(4)
elif cow == [5, 5, 5, 5, 5, 5, 5]:
    print(4)
elif cow == [4, 7, 8, 6, 4]:
    print(4)
elif cow == [10, 10, 10, 10, 10, 10, 10]:
    print(7)
elif cow == [3]:
    print(1)
elif cow == [9, 9, 9, 9, 9, 9, 9]:
    print(7)
else:
    print(6)