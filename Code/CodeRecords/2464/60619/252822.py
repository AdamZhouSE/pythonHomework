target = int(input())
num = input().split(",")
numbers = [int(i) for i in num]
lengths = []
for i in range(len(numbers)-1):
    current = numbers[i]
    le = 1
    for j in range(i+1, len(numbers)):
        current += numbers[j]
        le += 1
        if current >= target:
            lengths.append(le)
            break
if len(lengths) == 0:
    print(0)
else:
    lengths.sort()
    print(lengths[0])