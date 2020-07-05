input()
a = input()
b = input()
ans = 0
index = []
i = 0
j = 0
while i < len(b):
    start = i + 1
    j = 0
    while j < len(a):
        if a[j] == b[i] or a[j] == "*" or b[i] == "*":
            i += 1
            j += 1
            if j == len(a):
                ans += 1
                index.append(start)
        else:
            break
    i = start
print(ans)
for i in range(0, len(index)):
    print(index[i], end=" ")
print()
