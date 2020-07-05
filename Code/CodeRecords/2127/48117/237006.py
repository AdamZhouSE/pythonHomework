a = int(input())
bList = input().split(',')

b = 0
count = 0
for num in bList:
    num = int(num)
    b += num * pow(10, len(bList) - 1 - count)
    count += 1

print(pow(a, b) % 1337)