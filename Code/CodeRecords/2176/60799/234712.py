inp = input()
list_a = sorted([(inp[i:], i + 1) for i in range(0, len(inp))])
print(' '.join([str(i[1]) for i in list_a]))