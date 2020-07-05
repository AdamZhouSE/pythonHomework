input()
fish = list(map(int, input().split()))
ls = []
i = 0
while i != len(fish) - 1:
    ls.append(1)
    while fish[i] == fish[i + 1]:
        ls[-1] += 1
        i += 1
print(fish)
print(ls)
    