input()
a = input().split()
b = []
for i in range(len(a)):
    b.append(int(a[i]))
b.sort()

print(b[int(len(b)/2)])