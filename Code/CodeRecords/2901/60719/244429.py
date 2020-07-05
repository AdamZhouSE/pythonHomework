num = int(input())
i = 0
total = 0
if num % 2 == 0:
    i = 1
while total < num:
     total = total + 2 ** i
     i = i + 2
if total == num:
    print(True)
else:
    print(False)