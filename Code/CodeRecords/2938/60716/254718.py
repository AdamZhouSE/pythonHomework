lists = list()
for i in range(1,1000):
    lists.append(i)
strs = [str(i) for i in lists]
strs.sort()
for i in strs:
    print(i)