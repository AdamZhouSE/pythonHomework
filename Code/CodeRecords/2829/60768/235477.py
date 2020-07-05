size = int(input())
l = input().split(' ')
l = [int(x) for x in l]
l.sort()
if l[1] - l[0] > l[size - 1] - l[size - 2]:
    l.pop(0)
else:
    l.pop()
print(str(l[size - 2] - l[0]))
