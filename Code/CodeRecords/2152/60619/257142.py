length = int(input())
num = input().split(" ")
values = [int(i) for i in num]
teleports = [int(i)-1 for i in input().strip().split(" ")]
for i in range(length):
    start = i
    result = 0
    haveBeen = []
    while True:
        if start in haveBeen:
            break
        else:
            result += values[start]
            haveBeen.append(start)
            start = teleports[start]
    print(result)