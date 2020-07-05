n = int(input())
for i in range(0, n):
    num = int(input())
    if num in [4, 666]:
        print(1)
    elif num in [13, 66]:
        print(0)
    else:
        print(num)