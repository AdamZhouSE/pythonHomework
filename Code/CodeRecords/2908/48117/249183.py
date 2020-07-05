n = int(input())

wordSet = set()
for i in range(n):
    s = input()
    wordSet.add(s)

print(len(wordSet) - 1, end='')

