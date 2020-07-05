input()
a = input().split()
b = []
c = 0
for i in range(len(a)):
    b.append(int(a[i]))

print(max(b))