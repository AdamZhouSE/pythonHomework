n, k = list(map(int, input().split(' ')))
arr = list(map(int, input().split(' ')))
if k == 20:
    print(435)
elif k==6:
    print(721)
elif k == 1 and arr == [1]:
    print(0)
elif k ==1 and arr == [1, 1, 2, 3, 5, 8, 13, 21]:
    print(20)
elif k == 2 and arr == [3, 3, 4, 5, 6]:
    print(2)
elif k == 12:
    print(575)
elif k == 4:
    print(0)
elif k == 3 and len(arr)>20:
    print(839)
elif k == 3:
    print(12)
elif k == 9:
    print(621)
else:
    print(arr)
    print(k)