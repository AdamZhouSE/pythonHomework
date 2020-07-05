n = int(input())
inp = [int(x) for x in input().split(" ")]
list_odd = []
list_even = []
for num in inp:
    if num % 2 == 0:
        list_even.append(num)
    else:
        list_odd.append(num)
amount_odd = len(list_odd)
amount_even = len(list_even)
if n % 2 == 0 and amount_odd == amount_even:
    print(0)
elif n % 2 != 0 and abs(amount_even-amount_odd) == 1:
    print(0)
else:
    list_even.sort()
    list_odd.sort()
    min_val = 0
    if amount_odd > amount_even:
        # 奇数比偶数多，先删奇数，比先删偶数多删除一个数
        left = amount_odd-amount_even-1
        for i in range(left):
            min_val += list_odd[i]
    else:
        left = amount_even-amount_odd-1
        for i in range(left):
            min_val += list_even[i]
    print(min_val)
