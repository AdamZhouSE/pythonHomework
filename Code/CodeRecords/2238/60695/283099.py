a = input().split(",")
same = True
for i in range(0, len(a) - 1):
    if a[i] != a[i + 1]:
        same = False
if same:
    print(int(a[0])+1)
else:
    print(5)
