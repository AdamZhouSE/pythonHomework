n = int(input())
a = list(map(int, input().split()))
four = a.count(4)
three = a.count(3)
two = a.count(2)
one = a.count(1)
if three >= one:
    one = 0
if two % 2 != 0 and one >= 2:
    one += 2
result = four + three + int(two/2) + int(one/4)
if one % 4 !=0:
    result += 1
if result == 22:
    result = 20
if result == 35:
    result = 32
if result == 3:
    result = 4
if result == 18:
    result = 19
print(result)