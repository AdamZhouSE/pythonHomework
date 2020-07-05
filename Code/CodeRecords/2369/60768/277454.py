node = int(input())
s = input()
for i in range(node-1):
    current = input()
    s = s.replace(current[0], current)
s = s.replace('*', '')
print(s, end='')