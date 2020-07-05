n = int(input())
a = list(map(int, input().split()))
b = [[], []]
for x in a:
    b[x%2].append(x)
b[0].sort()
b[1].sort()
if abs(len(b[0]) - len(b[1])) <= 1:
    print(0)
elif len(b[0]) > len(b[1]):
    print(sum(b[0][0:len(b[0])-len(b[1])-1]))
else:
    print(sum(b[1][0:len(b[1])-len(b[0])-1]))