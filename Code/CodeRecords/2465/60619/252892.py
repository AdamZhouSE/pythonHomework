num = input().split(",")
numbers = [int(i) for i in num]
length = len(numbers)
i = length - 1
haveFind = False
while i >= 0:
    h = numbers[i]
    if 0 < length - h < i+1 and length - i <= h:
        print(h)
        haveFind = True
        break
    i -= 1
if not haveFind:
    print(-1)
