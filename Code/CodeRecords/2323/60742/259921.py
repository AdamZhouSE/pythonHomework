a = [int(i) for i in input().split(',')]
k = int(input())
a.sort()
max_dis = a[-1]-a[0]
if max_dis>2*k:
    print(max_dis-2*k)
else:
    print('0')