s = input()
s_list = {s[i:]: i + 1 for i in range(len(s))}
print(*[s_list.get(key) for key in sorted(s_list.keys())], end=' ')