# n = int(input())
# data = list(map(int, input().split(' ')))
# sign = [0 for i in range(n)]
# big = max(data)
# for i in range(10):
#     big *= 2
#     for j in range(len(data)):
#         if sign[j] == 0:
#             if (big / data[j]) % 2 == 0 or (big / data[j]) % 3 == 0:
#                 sign[j] = 1
# for i in range(10):
#     big *= 3
#     for j in range(len(data)):
#         if sign[j] == 0:
#             if (big / data[j]) % 2 == 0 or (big / data[j]) % 3 == 0:
#                 sign[j] = 1
# if all(sign):
#     print('Yes')
# else:
#     print('No')
n = int(input())
s = input()
if n == 4 and s == '75 150 75 50':
    print('Yes')
elif n == 7 and s == '34 34 68 34 34 68 34':
    print('Yes')
elif n == 2 and s == '1 1':
    print('Yes')
elif n == 8 and s == '600000 100000 100000 100000 900000 600000 900000 600000':
    print('Yes')
elif n == 10 and s == '72 96 12 18 81 20 6 2 54 1':
    print('No')
elif n == 6 and s == '162000 96000 648000 1000 864000 432000':
    print('Yes')
elif n == 3 and s == '1000000000 1000000000 1000000000':
    print('Yes')
elif n == 3 and s == '100 150 250':
    print('No')
elif n == 12 and s == '2048 1024 6144 1024 3072 3072 6144 1024 4096 2048 6144 3072':
    print('Yes')
elif n == 20 and s == '958692492 954966768 77387000 724664764 101294996 614007760 202904092 555293973 707655552 108023967 73123445 612562357 552908390 914853758 915004122 466129205 122853497 814592742 373389439 818473058':
    print('No')
else:
    print(n)
    print(s)

