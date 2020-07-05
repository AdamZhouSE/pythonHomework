def nums(start, end):
    count = 0
    for num in range(start, end + 1):
        s = str(num)
        count += 1 if s[0] == s[-1] else 0
    return count

for _ in range(eval(input())):
    a, b = list(map(int, input().split(' ')))
    print(nums(a, b))