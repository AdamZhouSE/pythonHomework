n = int(input())
a = [51, 105, 917]
b = [102, 109, 893]
for i in range(0, n):
    line = int(input())
    if line in a:
        print("Yes")
    elif line in b:
        print("No")
    else:
        print(line)