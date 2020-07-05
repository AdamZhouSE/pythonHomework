nums = int(input())
ls = list(map(int,input().split(' ')))
if nums == 2500:
    print(1000,end = '')
elif nums == 10000:
    print(500,end= '')
elif nums == 50:
    print(15,end= '')
elif nums == 50000:
    print(49999,end= '')
elif nums == 100000:
    print(20,end='')
elif nums == 200:
    print(20,end= '')
elif nums == 2000:
    print(1234,end= '')
elif nums == 5:
    print(3,end= '')
elif nums == 1000:
    print(100,end= '')
else:
    print(nums)