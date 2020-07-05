input()
fish = list(map(int, input().split()))
ls = []
i = 0
while i < len(fish) - 1:
    ls.append(1)
    while fish[i] == fish[i + 1]:
        ls[-1] += 1
        i += 1
        if i == len(fish) - 1:
            break
    i += 1
result = 0
for i in range(1, len(ls)):
    temp = min(ls[i], ls[i - 1])
    if temp > result:
        result = temp
print(result * 2)
    