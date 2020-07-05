num = int(input())
stairs = input().split(" ")
count = 0
count_stairs = []
for i in range(len(stairs) - 1):
    if stairs[i + 1] == '1':
        count += 1
        count_stairs.append(stairs[i])
count_stairs.append(stairs[num - 1])
count += 1
print(count)
print(" ".join(count_stairs))