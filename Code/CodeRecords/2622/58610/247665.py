a: list = eval(input())
try_num = a[0]
count = 0
for num in a:
    count += 1 if try_num == num else -1
    if count < 0:
        try_num = num
print(try_num)