a = list(map(int, input().replace('],[', ',').replace('[', '').replace(']', '').split(',')))
print(sorted(a, reverse=False))