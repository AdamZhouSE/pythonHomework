n = eval(input())
nums = list(map(int, input().split(' ')))
odds = sorted([x for x in nums if x % 2 == 1])
evens = sorted([x for x in nums if x % 2 == 0])
diff_len = abs(len(odds) - len(evens)) - 1
if diff_len <= 0:
    print(0)
elif len(odds) > len(evens):
    print(sum([odds[i] for i in range(diff_len)]))
else:
    print(sum([evens[i] for i in range(diff_len)]))