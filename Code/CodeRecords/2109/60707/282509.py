num = int(input())
if num == 0:
    print(str(0))
i = num % 9
if i==0:
    print(str(9))
else:
    print(str(i))