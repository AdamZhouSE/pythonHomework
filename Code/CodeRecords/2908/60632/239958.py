n = int(input())
words = []
for i in range(n):
    words.append(''.join(sorted(input().strip())))
print(len(set(words)), end='')
