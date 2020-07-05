def hasTwo(num):
    num = str(num)
    num = list(num)
    num.sort()
    num = ''.join(num)
    for i in range(0, len(num)):
        if num.count(num[i]) >= 2:
            return True
    return False


num = int(input())
count = 0
for i in range(11, num + 1):
    if hasTwo(i):
        count += 1
print(count)