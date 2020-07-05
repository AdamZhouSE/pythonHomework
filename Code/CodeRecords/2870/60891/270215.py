n = int(input())
a = [int(i) for i in input().split()]
a.sort()
max_s = 0
first_odd = 0
find_first_odd = False
for i in a:
    if find_first_odd is False and i % 2 == 1:
        find_first_odd = True
        first_odd = i
    max_s += i
if max_s % 2 == 1:
    max_s -= first_odd
print(max_s)