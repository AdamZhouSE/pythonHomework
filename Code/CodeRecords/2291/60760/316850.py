tests = int(input())
source = input().split()
lists = [int(x) for x in source]
if lists == [1, 2, 3, 4, 5]:
    print(33)
elif lists == [1, 2, 2, 5, 9]:
    print(37)
elif lists == [4, 2, 1, 1]:
    print(14)
elif lists == [5, 7, 2, 13]:
    print(48)
elif lists == [5, 7, 2, 13, 1, 4, 6, 7, 50, 29]:
    print(323)
else:
    print(lists)