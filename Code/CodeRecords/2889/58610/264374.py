num = eval(input())
bottles = list(map(int, input().split(' ')))
print('%.6f' % (sum(bottles) / num))