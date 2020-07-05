s = input("")
rank = list(range(1, len(s) + 1))
rank.sort(key = lambda x: s[x-1 : ])
print(' '.join([str(p) for p in rank]))
