import math
a = int(input())
temp = input().split(',')
b = int(''.join(str(i) for i in temp))
ans = math.pow(a,b)
print(str(int(ans % 1337)))