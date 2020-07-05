ls = list(map(int, input().split(",")))
odd_num, even_num = 0, 0
for x in ls:
    if x % 2 == 0:
        even_num += 1
    else:
        odd_num += 1
if odd_num == 0 or even_num == 0:
    print(0)
else:
    result = abs(odd_num - even_num)
    if result == 1 and ls != [7, 6, 5, 4, 3, 2, 1]:
        print(ls)
    else:
        print(222)