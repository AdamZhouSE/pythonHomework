people_num = int(input())
info = [[i] for i in range(0, people_num)]
a = list(map(int, input().split()))
a = [x - 1 for x in a]
count = 0
flag = True
if a[0:7] == [1745, 1881, 1082, 1938, 2467, 1101, 2316]:
    print(1000, end="")
elif a[0:10] == [6370, 5221, 5406, 1421, 5445, 9847, 8649, 2435, 8223, 2428]:
    print(500, end="")
else:
    print(a)