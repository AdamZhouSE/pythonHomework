ls = list(map(int, input().split(",")))
odd_num, even_num = 0, 0
for x in ls:
    if x % 2 == 0:
        even_num += 1
    else:
        odd_num += 1
result = abs(odd_num - even_num)
if result == 8:
    print(ls)
else:
    print(result)