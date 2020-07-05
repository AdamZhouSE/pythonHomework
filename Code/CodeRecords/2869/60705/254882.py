n = int(input())
a = list(map(int, input().split(" ")))
i = 0
while i < len(a):
    if a[i] in a[i+1:]:
        a.pop(i)
        i -= 1
    i += 1
print(len(a))
print(a[0], end="")
for i in a[1:]:
    print(" "+str(i), end="")

