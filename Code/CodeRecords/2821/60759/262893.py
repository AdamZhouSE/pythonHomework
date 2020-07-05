n = int(input())
lst = list(map(int, input().split(' ')))
choices = []
while len(lst) > 0:
    if lst[0] > lst[len(lst) - 1]:
        choices.append(lst[0])
        lst.pop(0)
    else:
        choices.append(lst[len(lst) - 1])
        lst.pop()
ans = str(sum([choices[i] for i in range(len(choices)) if not i % 2])) + ' ' + str(sum([choices[i] for i in range(len(choices)) if i % 2]))
print(ans)
