string = input()
# string = 'ababa'
ends = []
for i in range(len(string)):
    ends.append((i+1, string[i:]))
ends = sorted(ends, key=lambda x:x[1])
result = []
for group in ends:
    result.append(str(group[0]))
print(' '.join(result))
